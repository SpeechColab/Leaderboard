import pynini
from nemo_text_processing.text_normalization.zh.graph_utils import GraphFst,NEMO_NOT_QUOTE
from nemo_text_processing.text_normalization.zh.taggers.number import NumberFst
from pynini.lib import pynutil
class FractionFst(GraphFst):
    '''
        fraction { denominator: "5" numerator: "1" }  -> 五分之一      
    '''
    def __init__(self, deterministic: bool = True, lm: bool = False):
        super().__init__(name="fraction", kind="verbalize", deterministic=deterministic)   
        denominator = pynutil.delete("denominator: \"") + NumberFst().graph_number + pynutil.delete("\"")
        numerator = pynutil.delete("numerator: \"") + NumberFst().graph_number + pynutil.delete("\"") 
        frac_graph = denominator + pynutil.delete(" ") + pynutil.insert("分之") + numerator
        frac_graph = self.delete_tokens(frac_graph)
        self.fst = frac_graph.optimize()