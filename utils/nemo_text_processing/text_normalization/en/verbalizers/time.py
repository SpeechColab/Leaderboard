# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pynini
from nemo_text_processing.text_normalization.en.graph_utils import (
    NEMO_NOT_QUOTE,
    NEMO_SIGMA,
    GraphFst,
    delete_space,
    insert_space,
)
from pynini.lib import pynutil


class TimeFst(GraphFst):
    """
    Finite state transducer for verbalizing time, e.g.
        time { hours: "twelve" minutes: "thirty" suffix: "a m" zone: "e s t" } -> twelve thirty a m e s t
        time { hours: "twelve" } -> twelve o'clock

    Args:
        deterministic: if True will provide a single transduction option,
            for False multiple transduction are generated (used for audio-based normalization)
    """

    def __init__(self, deterministic: bool = True):
        super().__init__(name="time", kind="verbalize", deterministic=deterministic)
        hour = (
            pynutil.delete("hours:")
            + delete_space
            + pynutil.delete("\"")
            + pynini.closure(NEMO_NOT_QUOTE, 1)
            + pynutil.delete("\"")
        )
        minute = (
            pynutil.delete("minutes:")
            + delete_space
            + pynutil.delete("\"")
            + pynini.closure(NEMO_NOT_QUOTE, 1)
            + pynutil.delete("\"")
        )
        suffix = (
            pynutil.delete("suffix:")
            + delete_space
            + pynutil.delete("\"")
            + pynini.closure(NEMO_NOT_QUOTE, 1)
            + pynutil.delete("\"")
        )
        optional_suffix = pynini.closure(delete_space + insert_space + suffix, 0, 1)
        zone = (
            pynutil.delete("zone:")
            + delete_space
            + pynutil.delete("\"")
            + pynini.closure(NEMO_NOT_QUOTE, 1)
            + pynutil.delete("\"")
        )
        optional_zone = pynini.closure(delete_space + insert_space + zone, 0, 1)
        second = (
            pynutil.delete("seconds:")
            + delete_space
            + pynutil.delete("\"")
            + pynini.closure(NEMO_NOT_QUOTE, 1)
            + pynutil.delete("\"")
        )
        graph_hms = (
            hour
            + pynutil.insert(" hours ")
            + delete_space
            + minute
            + pynutil.insert(" minutes and ")
            + delete_space
            + second
            + pynutil.insert(" seconds")
            + optional_suffix
            + optional_zone
        )
        graph_hms @= pynini.cdrewrite(
            pynutil.delete("o ")
            | pynini.cross("one minutes", "one minute")
            | pynini.cross("one seconds", "one second")
            | pynini.cross("one hours", "one hour"),
            pynini.union(" ", "[BOS]"),
            "",
            NEMO_SIGMA,
        )
        graph = hour + delete_space + insert_space + minute + optional_suffix + optional_zone
        graph |= hour + insert_space + pynutil.insert("o'clock") + optional_zone
        graph |= hour + delete_space + insert_space + suffix + optional_zone
        graph |= graph_hms
        delete_tokens = self.delete_tokens(graph)
        self.fst = delete_tokens.optimize()
