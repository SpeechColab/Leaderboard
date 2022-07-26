import pynini
from nemo_text_processing.text_normalization.zh.graph_utils import NEMO_CHAR, GraphFst,NEMO_NOT_SPACE,NEMO_DIGIT,NEMO_ALPHA,NEMO_PUNCT
from pynini.lib import pynutil
from nemo_text_processing.text_normalization.zh.utils import get_abs_path,load_labels
class CharFst(GraphFst):
    '''
        你  ->   char { char: "你" }
        这儿 ->  char { er_char: "儿" }
        の  ->   char { other: "の" }
    '''
    def __init__(self, deterministic: bool = True, lm: bool = False):
        super().__init__(name="char", kind="classify", deterministic=deterministic)
        er = pynini.accep("儿")
        er_graph = pynutil.insert("er_char: \"") + er + pynutil.insert("\"")
        charset_std = pynini.string_file(get_abs_path("data/char/charset_national_standard_2013_8105.tsv"))
        charset_ext = pynini.string_file(get_abs_path("data/char/charset_extension.tsv"))

        charset_graph = pynini.union(charset_std , charset_ext)

        removal_char = pynini.string_file(get_abs_path("data/char/removal.tsv"))
        char_removal = pynutil.delete(removal_char)
        common_char = charset_graph|NEMO_DIGIT|NEMO_ALPHA|NEMO_PUNCT

        char = pynutil.insert("char: \"") + pynini.difference(common_char,er) + pynutil.insert("\"")
        char_other = pynutil.insert("other: \"") + pynini.difference(NEMO_CHAR,(common_char|er|pynini.accep(" "))) + pynutil.insert("\"")
        char|=er_graph
        char|= char_other
        char = self.add_tokens(char)
        self.char_removal = char_removal
        self.fst = char.optimize()