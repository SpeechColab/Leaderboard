import pynini
from nemo_text_processing.text_normalization.zh.graph_utils import NEMO_SIGMA, GraphFst, NEMO_NOT_QUOTE
from nemo_text_processing.text_normalization.zh.utils import get_abs_path
from pynini.lib import pynutil
class MeasureFst(GraphFst):
    '''
        measure { measure: "一千克" }  ->  一千克
    '''
    def __init__(self, deterministic: bool = True, lm: bool = False):
        super().__init__(name="measure", kind="verbalize", deterministic=deterministic)   
        graph_measure = pynutil.delete("measure: \"") + pynini.closure(NEMO_NOT_QUOTE) + pynutil.delete("\"")
        graph_measure = self.delete_tokens(graph_measure)
        self.fst = graph_measure.optimize()