import pynini
from nemo_text_processing.text_normalization.zh.graph_utils import NEMO_CHAR, GraphFst,NEMO_NOT_SPACE,NEMO_NOT_QUOTE
from pynini.lib import pynutil
from nemo_text_processing.text_normalization.zh.utils import get_abs_path
class CharFst(GraphFst):
    '''
        char { char: "你" }      -> 你
        char { er_char: "儿" }   -> ""
        char { other: "の" }     -> <の>
    '''
    def __init__(self, deterministic: bool = True, lm: bool = False):
        super().__init__(name="char", kind="verbalize", deterministic=deterministic)
        char = pynutil.delete("char: \"") + NEMO_NOT_SPACE + pynutil.delete("\"")
        er = pynutil.delete("er_char: \"") + pynutil.delete("儿") + pynutil.delete("\"")
        with open(get_abs_path("data/char/charset_illegal_tags.tsv"),"r") as f:
            line = f.readline()
            ltag = line[0]
            rtag = line[2]
        char_other = pynutil.delete("other: \"") + pynutil.insert(ltag) + NEMO_CHAR  + pynutil.insert(rtag) + pynutil.delete("\"") 
        char|=er
        char|=char_other
        char = self.delete_tokens(char)
        self.fst = char.optimize()