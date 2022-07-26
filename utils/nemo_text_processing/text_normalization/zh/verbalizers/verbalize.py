from nemo_text_processing.text_normalization.zh.graph_utils import GraphFst
from nemo_text_processing.text_normalization.zh.verbalizers.date import DateFst
from nemo_text_processing.text_normalization.zh.verbalizers.number import NumberFst
from nemo_text_processing.text_normalization.zh.verbalizers.char import CharFst
from nemo_text_processing.text_normalization.zh.verbalizers.fraction import FractionFst
from nemo_text_processing.text_normalization.zh.verbalizers.percent import PercentFst
from nemo_text_processing.text_normalization.zh.verbalizers.math import MathSymbolFst
from nemo_text_processing.text_normalization.zh.verbalizers.money import MoneyFst
from nemo_text_processing.text_normalization.zh.verbalizers.measure import MeasureFst
from nemo_text_processing.text_normalization.zh.verbalizers.time import TimeFst
from nemo_text_processing.text_normalization.zh.verbalizers.erhua_removal import ErhuaRemovalFst
# from nemo_text_processing.text_normalization.zh.verbalizers.halfwidth import HalfwidthFst
from nemo_text_processing.text_normalization.zh.verbalizers.whitelist import WhitelistFst
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

        date = DateFst(deterministic=deterministic)
        date_graph = date.fst

        number = NumberFst(deterministic=deterministic)
        number_graph = number.fst
        
        char = CharFst(deterministic=deterministic)
        char_graph = char.fst

        fraction = FractionFst(deterministic=deterministic)
        fraction_graph = fraction.fst

        percent = PercentFst(deterministic=deterministic)
        percent_graph = percent.fst

        math_symbol = MathSymbolFst(deterministic=deterministic)
        math_symbol_graph = math_symbol.fst

        money = MoneyFst(deterministic=deterministic)
        money_graph = money.fst

        measure = MeasureFst(deterministic=deterministic)
        measure_graph = measure.fst

        time = TimeFst(deterministic=deterministic)
        time_graph = time.fst

        erhua = ErhuaRemovalFst(deterministic=deterministic)
        erhua_graph = erhua.fst

        
        whitelist = WhitelistFst(deterministic=deterministic)
        whitelist_graph = whitelist.fst
        graph = ( 
        	date_graph
            |number_graph
            |fraction_graph
            |char_graph
            |math_symbol_graph
            |percent_graph
            |money_graph
            |measure_graph
            |time_graph
            |erhua_graph
            |whitelist_graph
        )
        self.fst = graph
