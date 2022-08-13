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

import sys
from unicodedata import category

import pynini
from nemo_text_processing.text_normalization.en.graph_utils import NEMO_NOT_SPACE, NEMO_SIGMA, GraphFst
from nemo_text_processing.text_normalization.en.utils import get_abs_path, load_labels
from pynini.examples import plurals
from pynini.lib import pynutil


class PunctuationFst(GraphFst):
    """
    Finite state transducer for classifying punctuation
        e.g. a, -> tokens { name: "a" } tokens { name: "," }

    Args:
        deterministic: if True will provide a single transduction option,
            for False multiple transduction are generated (used for audio-based normalization)

    """

    def __init__(self, deterministic: bool = True):
        super().__init__(name="punctuation", kind="classify", deterministic=deterministic)
        s = "!#%&\'()*+,-./:;<=>?@^_`{|}~\""

        punct_symbols_to_exclude = ["[", "]"]
        punct_unicode = [
            chr(i)
            for i in range(sys.maxunicode)
            if category(chr(i)).startswith("P") and chr(i) not in punct_symbols_to_exclude
        ]

        whitelist_symbols = load_labels(get_abs_path("data/whitelist/symbol.tsv"))
        whitelist_symbols = [x[0] for x in whitelist_symbols]
        self.punct_marks = [p for p in punct_unicode + list(s) if p not in whitelist_symbols]

        punct = pynini.union(*self.punct_marks)
        punct = pynini.closure(punct, 1)

        emphasis = (
            pynini.accep("<")
            + (
                (pynini.closure(NEMO_NOT_SPACE - pynini.union("<", ">"), 1) + pynini.closure(pynini.accep("/"), 0, 1))
                | (pynini.accep("/") + pynini.closure(NEMO_NOT_SPACE - pynini.union("<", ">"), 1))
            )
            + pynini.accep(">")
        )
        punct = plurals._priority_union(emphasis, punct, NEMO_SIGMA)

        self.graph = punct
        self.fst = (pynutil.insert("name: \"") + self.graph + pynutil.insert("\"")).optimize()
