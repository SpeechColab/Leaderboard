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
    NEMO_DIGIT,
    NEMO_NOT_QUOTE,
    NEMO_SIGMA,
    GraphFst,
    insert_space,
)
from nemo_text_processing.text_normalization.en.taggers.date import get_four_digit_year_graph
from nemo_text_processing.text_normalization.en.utils import get_abs_path
from pynini.examples import plurals
from pynini.lib import pynutil


class CardinalFst(GraphFst):
    """
    Finite state transducer for classifying cardinals, e.g. 
        -23 -> cardinal { negative: "true"  integer: "twenty three" } }

    Args:
        deterministic: if True will provide a single transduction option,
            for False multiple transduction are generated (used for audio-based normalization)
    """

    def __init__(self, deterministic: bool = True, lm: bool = False):
        super().__init__(name="cardinal", kind="classify", deterministic=deterministic)

        self.lm = lm
        self.deterministic = deterministic
        # TODO replace to have "oh" as a default for "0"
        graph = pynini.Far(get_abs_path("data/number/cardinal_number_name.far")).get_fst()
        self.graph_hundred_component_at_least_one_none_zero_digit = (
            pynini.closure(NEMO_DIGIT, 2, 3) | pynini.difference(NEMO_DIGIT, pynini.accep("0"))
        ) @ graph

        graph_digit = pynini.string_file(get_abs_path("data/number/digit.tsv"))
        graph_zero = pynini.string_file(get_abs_path("data/number/zero.tsv"))

        single_digits_graph = pynini.invert(graph_digit | graph_zero)
        self.single_digits_graph = single_digits_graph + pynini.closure(insert_space + single_digits_graph)

        if not deterministic:
            # for a single token allow only the same normalization
            # "007" -> {"oh oh seven", "zero zero seven"} not {"oh zero seven"}
            single_digits_graph_zero = pynini.invert(graph_digit | graph_zero)
            single_digits_graph_oh = pynini.invert(graph_digit) | pynini.cross("0", "oh")

            self.single_digits_graph = single_digits_graph_zero + pynini.closure(
                insert_space + single_digits_graph_zero
            )
            self.single_digits_graph |= single_digits_graph_oh + pynini.closure(insert_space + single_digits_graph_oh)

            single_digits_graph_with_commas = pynini.closure(
                self.single_digits_graph + insert_space, 1, 3
            ) + pynini.closure(
                pynutil.delete(",")
                + single_digits_graph
                + insert_space
                + single_digits_graph
                + insert_space
                + single_digits_graph,
                1,
            )

        optional_minus_graph = pynini.closure(pynutil.insert("negative: ") + pynini.cross("-", "\"true\" "), 0, 1)

        graph = (
            pynini.closure(NEMO_DIGIT, 1, 3)
            + (pynini.closure(pynutil.delete(",") + NEMO_DIGIT ** 3) | pynini.closure(NEMO_DIGIT ** 3))
        ) @ graph

        self.graph = graph
        self.graph_with_and = self.add_optional_and(graph)

        if deterministic:
            long_numbers = pynini.compose(NEMO_DIGIT ** (5, ...), self.single_digits_graph).optimize()
            final_graph = plurals._priority_union(long_numbers, self.graph_with_and, NEMO_SIGMA).optimize()
            cardinal_with_leading_zeros = pynini.compose(
                pynini.accep("0") + pynini.closure(NEMO_DIGIT), self.single_digits_graph
            )
            final_graph |= cardinal_with_leading_zeros
        else:
            leading_zeros = pynini.compose(pynini.closure(pynini.accep("0"), 1), self.single_digits_graph)
            cardinal_with_leading_zeros = (
                leading_zeros + pynutil.insert(" ") + pynini.compose(pynini.closure(NEMO_DIGIT), self.graph_with_and)
            )

            # add small weight to non-default graphs to make sure the deterministic option is listed first
            final_graph = (
                self.graph_with_and
                | pynutil.add_weight(self.single_digits_graph, 0.0001)
                | get_four_digit_year_graph()  # allows e.g. 4567 be pronouced as forty five sixty seven
                | pynutil.add_weight(single_digits_graph_with_commas, 0.0001)
                | cardinal_with_leading_zeros
            )

        final_graph = optional_minus_graph + pynutil.insert("integer: \"") + final_graph + pynutil.insert("\"")
        final_graph = self.add_tokens(final_graph)
        self.fst = final_graph.optimize()

    def add_optional_and(self, graph):
        graph_with_and = graph

        if not self.lm:
            graph_with_and = pynutil.add_weight(graph, 0.00001)
            not_quote = pynini.closure(NEMO_NOT_QUOTE)
            no_thousand_million = pynini.difference(
                not_quote, not_quote + pynini.union("thousand", "million") + not_quote
            ).optimize()
            integer = (
                not_quote + pynutil.add_weight(pynini.cross("hundred ", "hundred and ") + no_thousand_million, -0.0001)
            ).optimize()

            no_hundred = pynini.difference(NEMO_SIGMA, not_quote + pynini.accep("hundred") + not_quote).optimize()
            integer |= (
                not_quote + pynutil.add_weight(pynini.cross("thousand ", "thousand and ") + no_hundred, -0.0001)
            ).optimize()

            optional_hundred = pynini.compose((NEMO_DIGIT - "0") ** 3, graph).optimize()
            optional_hundred = pynini.compose(optional_hundred, NEMO_SIGMA + pynini.cross(" hundred", "") + NEMO_SIGMA)
            graph_with_and |= pynini.compose(graph, integer).optimize()
            graph_with_and |= optional_hundred
        return graph_with_and
