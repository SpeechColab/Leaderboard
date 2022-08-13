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
from nemo_text_processing.text_normalization.en.graph_utils import NEMO_NOT_QUOTE, GraphFst
from pynini.lib import pynutil


class AbbreviationFst(GraphFst):
    """
    Finite state transducer for verbalizing abbreviations
        e.g. tokens { abbreviation { value: "A B C" } } -> "ABC"

    Args:
        deterministic: if True will provide a single transduction option,
            for False multiple transduction are generated (used for audio-based normalization)
    """

    def __init__(self, deterministic: bool = True):
        super().__init__(name="abbreviation", kind="verbalize", deterministic=deterministic)

        graph = pynutil.delete("value: \"") + pynini.closure(NEMO_NOT_QUOTE, 1) + pynutil.delete("\"")
        delete_tokens = self.delete_tokens(graph)
        self.fst = delete_tokens.optimize()
