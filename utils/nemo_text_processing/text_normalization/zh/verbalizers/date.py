import pynini
from nemo_text_processing.text_normalization.zh.graph_utils import NEMO_SIGMA, NEMO_NOT_QUOTE ,GraphFst
from nemo_text_processing.text_normalization.zh.utils import get_abs_path,UNIT_1e01
from pynini.lib import pynutil
class DateFst(GraphFst):
    '''
        date { year: "2002" month: "01" day: "28"}  ->  二零零二年一月二十八日
        date { year: "2002" }                       ->  二零零八年
    '''
    def __init__(self, deterministic: bool = True, lm: bool = False):
        super().__init__(name="date", kind="verbalize", deterministic=deterministic)
        date_type0 = pynutil.delete('year: \"') + pynini.closure(NEMO_NOT_QUOTE) + pynutil.delete('\"') 
        graph_digit = pynini.string_file(get_abs_path("data/number/digit.tsv"))
        graph_ten = pynini.string_file(get_abs_path("data/number/digit_teen.tsv"))
        graph_zero = pynini.string_file(get_abs_path("data/number/zero.tsv"))
        graph_no_zero = pynini.cross("0","")
        graph_year = pynini.closure(graph_digit|graph_zero,2,4)
        graph_digit_no_zero = graph_digit|graph_no_zero
        graph_2_digit_date = (
             (graph_ten + pynutil.insert(UNIT_1e01) + graph_digit_no_zero)|
            (graph_no_zero + graph_digit)
        )

        date_type1 = pynutil.delete("year: \"") + graph_year + pynutil.insert("年") + pynutil.delete("\"") + " "\
                    + pynutil.delete("month: \"") + graph_2_digit_date + pynutil.insert("月") + pynutil.delete("\"") + " "\
                    + pynutil.delete("day: \"") + graph_2_digit_date + pynutil.insert("日") + pynutil.delete("\"")

        date_type2 = pynutil.delete("year: \"") + graph_year + pynutil.insert("年") + pynutil.delete("\"") + " "\
                    + pynutil.delete("month: \"") + graph_2_digit_date + pynutil.insert("月") + pynutil.delete("\"")

        graoh_date = date_type0|date_type1|date_type2
        delete_tokens = self.delete_tokens(graoh_date)
        self.fst = delete_tokens.optimize()
