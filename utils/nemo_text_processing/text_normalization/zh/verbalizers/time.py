import pynini
from nemo_text_processing.text_normalization.zh.graph_utils import NEMO_SIGMA, GraphFst, insert_space,NEMO_DIGIT,NEMO_NOT_QUOTE
from nemo_text_processing.text_normalization.zh.utils import get_abs_path,UNIT_1e01
from pynini.lib import pynutil
class TimeFst(GraphFst):
    '''
        time { h: "1" m: "02" s: "36" }  ->  一点零二分三十六秒
    '''
    def __init__(self, deterministic: bool = True, lm: bool = False):
        super().__init__(name="time", kind="verbalize", deterministic=deterministic)  
        graph_digit = pynini.string_file(get_abs_path("data/number/digit.tsv"))
        graph_ten = pynini.string_file(get_abs_path("data/number/digit_teen.tsv"))
        graph_zero = pynini.string_file(get_abs_path("data/number/zero.tsv"))
        graph_no_zero = pynini.cross("0","")

        graph_digit_no_zero = graph_digit|graph_no_zero
        graph_2_digit_time = (
             (graph_ten + pynutil.insert(UNIT_1e01) + graph_digit_no_zero)|
            (graph_zero + graph_digit)
        )
        graph_2_digit_zero_none = pynini.cross("0","") + pynini.cross("0","")
        graph_2_digit_zero = pynini.cross("00","零")
        h = graph_2_digit_time|graph_2_digit_zero|graph_digit
        m = graph_2_digit_time|graph_2_digit_zero
        # 6:25
        h_m = pynutil.delete("h: \"") + h + pynutil.insert("点")+ pynutil.delete("\"") + \
                " "\
                + pynutil.delete("m: \"") + (graph_2_digit_time) + pynutil.insert("分") + pynutil.delete("\"")
        # 23:00
        h_00 = pynutil.delete("h: \"") + h +pynutil.insert("点")+ pynutil.delete("\"") +\
                 " "\
                + pynutil.delete("m: \"") + (graph_2_digit_zero_none) + pynutil.delete("\"")
        # 9:12:52
        h_m_s = pynutil.delete("h: \"") + h + pynutil.insert("点")+ pynutil.delete("\"") + \
                 " "\
                + pynutil.delete("m: \"") + m + pynutil.insert("分")+ pynutil.delete("\"") + \
                " " + \
                pynutil.delete("s: \"") + (graph_2_digit_time) + pynutil.insert("秒") + pynutil.delete("\"")
        clock_graph = h_m|h_m_s|h_00

        graph_time = clock_graph
        graph_time = self.delete_tokens(graph_time)
        self.fst = graph_time.optimize()