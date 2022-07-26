import pynini
from nemo_text_processing.text_normalization.zh.graph_utils import NEMO_SIGMA, GraphFst, insert_space,NEMO_DIGIT
from nemo_text_processing.text_normalization.zh.utils import get_abs_path
from nemo_text_processing.text_normalization.zh.taggers.number import NumberFst
from pynini.lib import pynutil
class MoneyFst(GraphFst):
    '''
        ￥1.25 --> money { cur: "元" num: "一点五" }
    '''
    def __init__(self, deterministic: bool = True, lm: bool = False):
        super().__init__(name="money", kind="classify", deterministic=deterministic)
        currency_graph = pynini.string_file(get_abs_path("data/money/currency.tsv"))  
        final_graph = pynutil.insert("cur: \"") + currency_graph + pynutil.insert("\"") + insert_space\
                        + pynutil.insert("num: \"") + NumberFst().graph_number + pynutil.insert("\"")
        final_graph = self.add_tokens(final_graph)
        self.fst = final_graph.optimize()
        

