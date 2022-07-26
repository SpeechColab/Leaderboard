import pynini
from nemo_text_processing.text_normalization.zh.graph_utils import GraphFst,insert_space,NEMO_DIGIT,NEMO_NOT_QUOTE
from nemo_text_processing.text_normalization.zh.taggers.number import NumberFst
from pynini.lib import pynutil
class PercentFst(GraphFst):
    '''
        1.5%  -> percent { percent: "1.5" }      
    '''
    def __init__(self, deterministic: bool = True, lm: bool = False):
        super().__init__(name="percent", kind="classify", deterministic=deterministic)        
        
        percent_graph = pynutil.insert("percent: \"") + NumberFst().graph_number + \
                        pynutil.delete("%") + pynutil.insert("\"") 
        percent_graph = self.add_tokens(percent_graph)
        self.fst = percent_graph.optimize()