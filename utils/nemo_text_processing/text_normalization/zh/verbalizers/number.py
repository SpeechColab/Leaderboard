import pynini
from nemo_text_processing.text_normalization.zh.graph_utils import GraphFst,NEMO_NOT_QUOTE
from pynini.lib import pynutil
class NumberFst(GraphFst):
    '''
        number { number: "123"}  ->  一二三
    '''
    def __init__(self, deterministic: bool = True, lm: bool = False):
        super().__init__(name="number", kind="verbalize", deterministic=deterministic)
        number_graph = pynutil.delete('number: \"') + pynini.closure(NEMO_NOT_QUOTE) + pynutil.delete('\"') 
        delete_tokens = self.delete_tokens(number_graph)
        self.fst = delete_tokens.optimize()