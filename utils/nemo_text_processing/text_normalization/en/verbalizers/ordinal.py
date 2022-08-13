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
from nemo_text_processing.text_normalization.en.graph_utils import NEMO_NOT_QUOTE, NEMO_SIGMA, GraphFst, delete_space
from nemo_text_processing.text_normalization.en.utils import get_abs_path
from pynini.lib import pynutil


class OrdinalFst(GraphFst):
    """
    Finite state transducer for verbalizing ordinal, e.g.
        ordinal { integer: "thirteen" } } -> thirteenth

    Args:
        deterministic: if True will provide a single transduction option,
            for False multiple transduction are generated (used for audio-based normalization)
    """

    def __init__(self, deterministic: bool = True):
        super().__init__(name="ordinal", kind="verbalize", deterministic=deterministic)

        graph_digit = pynini.string_file(get_abs_path("data/ordinal/digit.tsv")).invert()
        graph_teens = pynini.string_file(get_abs_path("data/ordinal/teen.tsv")).invert()

        graph = (
            pynutil.delete("integer:")
            + delete_space
            + pynutil.delete("\"")
            + pynini.closure(NEMO_NOT_QUOTE, 1)
            + pynutil.delete("\"")
        )
        convert_rest = pynutil.insert("th")

        suffix = pynini.cdrewrite(
            graph_digit | graph_teens | pynini.cross("ty", "tieth") | convert_rest, "", "[EOS]", NEMO_SIGMA,
        ).optimize()
        self.graph = pynini.compose(graph, suffix)
        self.suffix = suffix
        delete_tokens = self.delete_tokens(self.graph)
        self.fst = delete_tokens.optimize()
