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

from nemo_text_processing.text_normalization.en.graph_utils import GraphFst
from nemo_text_processing.text_normalization.en.verbalizers.abbreviation import AbbreviationFst
from nemo_text_processing.text_normalization.en.verbalizers.cardinal import CardinalFst
from nemo_text_processing.text_normalization.en.verbalizers.date import DateFst
from nemo_text_processing.text_normalization.en.verbalizers.decimal import DecimalFst
from nemo_text_processing.text_normalization.en.verbalizers.electronic import ElectronicFst
from nemo_text_processing.text_normalization.en.verbalizers.fraction import FractionFst
from nemo_text_processing.text_normalization.en.verbalizers.measure import MeasureFst
from nemo_text_processing.text_normalization.en.verbalizers.money import MoneyFst
from nemo_text_processing.text_normalization.en.verbalizers.ordinal import OrdinalFst
from nemo_text_processing.text_normalization.en.verbalizers.roman import RomanFst
from nemo_text_processing.text_normalization.en.verbalizers.telephone import TelephoneFst
from nemo_text_processing.text_normalization.en.verbalizers.time import TimeFst
from nemo_text_processing.text_normalization.en.verbalizers.whitelist import WhiteListFst


class VerbalizeFst(GraphFst):
    """
    Composes other verbalizer grammars.
    For deployment, this grammar will be compiled and exported to OpenFst Finate State Archiv (FAR) File. 
    More details to deployment at NeMo/tools/text_processing_deployment.

    Args:
        deterministic: if True will provide a single transduction option,
            for False multiple options (used for audio-based normalization)
    """

    def __init__(self, deterministic: bool = True):
        super().__init__(name="verbalize", kind="verbalize", deterministic=deterministic)
        cardinal = CardinalFst(deterministic=deterministic)
        cardinal_graph = cardinal.fst
        decimal = DecimalFst(cardinal=cardinal, deterministic=deterministic)
        decimal_graph = decimal.fst
        ordinal = OrdinalFst(deterministic=deterministic)
        ordinal_graph = ordinal.fst
        fraction = FractionFst(deterministic=deterministic)
        fraction_graph = fraction.fst
        telephone_graph = TelephoneFst(deterministic=deterministic).fst
        electronic_graph = ElectronicFst(deterministic=deterministic).fst
        measure = MeasureFst(decimal=decimal, cardinal=cardinal, fraction=fraction, deterministic=deterministic)
        measure_graph = measure.fst
        time_graph = TimeFst(deterministic=deterministic).fst
        date_graph = DateFst(ordinal=ordinal, deterministic=deterministic).fst
        money_graph = MoneyFst(decimal=decimal, deterministic=deterministic).fst
        whitelist_graph = WhiteListFst(deterministic=deterministic).fst

        graph = (
            time_graph
            | date_graph
            | money_graph
            | measure_graph
            | ordinal_graph
            | decimal_graph
            | cardinal_graph
            | telephone_graph
            | electronic_graph
            | fraction_graph
            | whitelist_graph
        )

        roman_graph = RomanFst(deterministic=deterministic).fst
        graph |= roman_graph

        if not deterministic:
            abbreviation_graph = AbbreviationFst(deterministic=deterministic).fst
            graph |= abbreviation_graph

        self.fst = graph
