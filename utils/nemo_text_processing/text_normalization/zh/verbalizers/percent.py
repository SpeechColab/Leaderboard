import pynini
from nemo_text_processing.text_normalization.zh.graph_utils import GraphFst,insert_space,NEMO_DIGIT,NEMO_NOT_QUOTE
from nemo_text_processing.text_normalization.zh.taggers.number import NumberFst
from pynini.lib import pynutil
class PercentFst(GraphFst):
    '''
        percent { percent: "1.5" }  ->  百分之一点五
    '''
    def __init__(self, deterministic: bool = True, lm: bool = False):
        super().__init__(name="percent", kind="verbalize", deterministic=deterministic)   
        percent_graph = pynutil.delete("percent: \"") + pynini.closure(NEMO_NOT_QUOTE,1) + pynutil.delete("\"")
        percent_graph = pynutil.insert("百分之") + percent_graph
        percent_graph = self.delete_tokens(percent_graph)
        self.fst = percent_graph.optimize()