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

import os
import time

import pynini
from nemo_text_processing.text_normalization.en.graph_utils import (
    NEMO_WHITE_SPACE,
    GraphFst,
    delete_extra_space,
    delete_space,
    generator_main,
)
from nemo_text_processing.text_normalization.en.taggers.abbreviation import AbbreviationFst
from nemo_text_processing.text_normalization.en.taggers.cardinal import CardinalFst
from nemo_text_processing.text_normalization.en.taggers.date import DateFst
from nemo_text_processing.text_normalization.en.taggers.decimal import DecimalFst
from nemo_text_processing.text_normalization.en.taggers.electronic import ElectronicFst
from nemo_text_processing.text_normalization.en.taggers.fraction import FractionFst
from nemo_text_processing.text_normalization.en.taggers.measure import MeasureFst
from nemo_text_processing.text_normalization.en.taggers.money import MoneyFst
from nemo_text_processing.text_normalization.en.taggers.ordinal import OrdinalFst
from nemo_text_processing.text_normalization.en.taggers.punctuation import PunctuationFst
from nemo_text_processing.text_normalization.en.taggers.range import RangeFst as RangeFst
from nemo_text_processing.text_normalization.en.taggers.roman import RomanFst
from nemo_text_processing.text_normalization.en.taggers.serial import SerialFst
from nemo_text_processing.text_normalization.en.taggers.telephone import TelephoneFst
from nemo_text_processing.text_normalization.en.taggers.time import TimeFst
from nemo_text_processing.text_normalization.en.taggers.whitelist import WhiteListFst
from nemo_text_processing.text_normalization.en.taggers.word import WordFst
from nemo_text_processing.text_normalization.en.verbalizers.date import DateFst as vDateFst
from nemo_text_processing.text_normalization.en.verbalizers.ordinal import OrdinalFst as vOrdinalFst
from nemo_text_processing.text_normalization.en.verbalizers.time import TimeFst as vTimeFst
from pynini.lib import pynutil



class ClassifyFst(GraphFst):
    """
    Final class that composes all other classification grammars. This class can process an entire sentence including punctuation.
    For deployment, this grammar will be compiled and exported to OpenFst Finate State Archiv (FAR) File. 
    More details to deployment at NeMo/tools/text_processing_deployment.
    
    Args:
        input_case: accepting either "lower_cased" or "cased" input.
        deterministic: if True will provide a single transduction option,
            for False multiple options (used for audio-based normalization)
        cache_dir: path to a dir with .far grammar file. Set to None to avoid using cache.
        overwrite_cache: set to True to overwrite .far files
        whitelist: path to a file with whitelist replacements
    """

    def __init__(
        self,
        input_case: str,
        deterministic: bool = True,
        cache_dir: str = None,
        overwrite_cache: bool = False,
        whitelist: str = None,
    ):
        super().__init__(name="tokenize_and_classify", kind="classify", deterministic=deterministic)

        far_file = None
        if cache_dir is not None and cache_dir != "None":
            os.makedirs(cache_dir, exist_ok=True)
            whitelist_file = os.path.basename(whitelist) if whitelist else ""
            far_file = os.path.join(
                cache_dir, f"en_tn_{deterministic}_deterministic_{input_case}_{whitelist_file}_tokenize.far"
            )
        if not overwrite_cache and far_file and os.path.exists(far_file):
            self.fst = pynini.Far(far_file, mode="r")["tokenize_and_classify"]
        else:

            start_time = time.time()
            cardinal = CardinalFst(deterministic=deterministic)
            cardinal_graph = cardinal.fst

            start_time = time.time()
            ordinal = OrdinalFst(cardinal=cardinal, deterministic=deterministic)
            ordinal_graph = ordinal.fst

            start_time = time.time()
            decimal = DecimalFst(cardinal=cardinal, deterministic=deterministic)
            decimal_graph = decimal.fst

            start_time = time.time()
            fraction = FractionFst(deterministic=deterministic, cardinal=cardinal)
            fraction_graph = fraction.fst

            start_time = time.time()
            measure = MeasureFst(cardinal=cardinal, decimal=decimal, fraction=fraction, deterministic=deterministic)
            measure_graph = measure.fst

            start_time = time.time()
            date_graph = DateFst(cardinal=cardinal, deterministic=deterministic).fst

            start_time = time.time()
            time_graph = TimeFst(cardinal=cardinal, deterministic=deterministic).fst

            start_time = time.time()
            telephone_graph = TelephoneFst(deterministic=deterministic).fst

            start_time = time.time()
            electonic_graph = ElectronicFst(deterministic=deterministic).fst

            start_time = time.time()
            money_graph = MoneyFst(cardinal=cardinal, decimal=decimal, deterministic=deterministic).fst


            start_time = time.time()
            whitelist_graph = WhiteListFst(
                input_case=input_case, deterministic=deterministic, input_file=whitelist
            ).fst

            start_time = time.time()
            punctuation = PunctuationFst(deterministic=deterministic)
            punct_graph = punctuation.fst

            start_time = time.time()
            word_graph = WordFst(punctuation=punctuation, deterministic=deterministic).fst
            

            start_time = time.time()
            serial_graph = SerialFst(cardinal=cardinal, ordinal=ordinal, deterministic=deterministic).fst
            

            start_time = time.time()
            v_time_graph = vTimeFst(deterministic=deterministic).fst
            v_ordinal_graph = vOrdinalFst(deterministic=deterministic)
            v_date_graph = vDateFst(ordinal=v_ordinal_graph, deterministic=deterministic).fst
            time_final = pynini.compose(time_graph, v_time_graph)
            date_final = pynini.compose(date_graph, v_date_graph)
            range_graph = RangeFst(
                time=time_final, date=date_final, cardinal=cardinal, deterministic=deterministic
            ).fst
            

            classify = (
                pynutil.add_weight(whitelist_graph, 1.01)
                | pynutil.add_weight(time_graph, 1.1)
                | pynutil.add_weight(date_graph, 1.09)
                | pynutil.add_weight(decimal_graph, 1.1)
                | pynutil.add_weight(measure_graph, 1.1)
                | pynutil.add_weight(cardinal_graph, 1.1)
                | pynutil.add_weight(ordinal_graph, 1.1)
                | pynutil.add_weight(money_graph, 1.1)
                | pynutil.add_weight(telephone_graph, 1.1)
                | pynutil.add_weight(electonic_graph, 1.1)
                | pynutil.add_weight(fraction_graph, 1.1)
                | pynutil.add_weight(range_graph, 1.1)
                | pynutil.add_weight(serial_graph, 1.1001)  # should be higher than the rest of the classes
            )

            roman_graph = RomanFst(deterministic=deterministic).fst
            classify |= pynutil.add_weight(roman_graph, 1.1)

            if not deterministic:
                abbreviation_graph = AbbreviationFst(deterministic=deterministic).fst
                classify |= pynutil.add_weight(abbreviation_graph, 100)

            punct = pynutil.insert("tokens { ") + pynutil.add_weight(punct_graph, weight=2.1) + pynutil.insert(" }")
            punct = pynini.closure(
                pynini.compose(pynini.closure(NEMO_WHITE_SPACE, 1), delete_extra_space)
                | (pynutil.insert(" ") + punct),
                1,
            )

            classify |= pynutil.add_weight(word_graph, 100)
            token = pynutil.insert("tokens { ") + classify + pynutil.insert(" }")
            token_plus_punct = (
                pynini.closure(punct + pynutil.insert(" ")) + token + pynini.closure(pynutil.insert(" ") + punct)
            )

            graph = token_plus_punct + pynini.closure(
                (
                    pynini.compose(pynini.closure(NEMO_WHITE_SPACE, 1), delete_extra_space)
                    | (pynutil.insert(" ") + punct + pynutil.insert(" "))
                )
                + token_plus_punct
            )

            graph = delete_space + graph + delete_space
            graph |= punct

            self.fst = graph.optimize()

            if far_file:
                generator_main(far_file, {"tokenize_and_classify": self.fst})
                
