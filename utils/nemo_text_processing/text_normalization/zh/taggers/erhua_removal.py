import pynini
from nemo_text_processing.text_normalization.zh.graph_utils import NEMO_SIGMA, GraphFst,NEMO_NOT_SPACE
from pynini.lib import pynutil
from nemo_text_processing.text_normalization.zh.utils import get_abs_path,load_labels
class ErhuaRemovalFst(GraphFst):
    '''
        女儿  -  erhua { erhua: "女儿" }
    '''
    def __init__(self, deterministic: bool = True, lm: bool = False):
        super().__init__(name="erhua", kind="classify", deterministic=deterministic)
        whitelist = pynini.string_map(load_labels(get_abs_path("data/char/erhua_removal_whitelist.tsv")))
        erhua_graph = whitelist       
        erhua_white = pynutil.insert("erhua: \"") + erhua_graph + pynutil.insert("\"")
        erhua_white = self.add_tokens(erhua_white)
        self.fst = erhua_white.optimize()