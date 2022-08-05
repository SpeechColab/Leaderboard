import csv
import os
import pynini
from pynini.lib import pynutil,utf8
import string

def get_abs_path(rel_path):
    """
    Get absolute path
    Args:
        rel_path: relative path to this file
        
    Returns absolute path
    """
    return os.path.dirname(os.path.abspath(__file__)) + '/' + rel_path


def load_labels(abs_path):
    """
    loads relative path file as dictionary
    Args:
        abs_path: absolute path
    Returns dictionary of mappings
    """
    label_tsv = open(abs_path, encoding="utf-8")
    labels = list(csv.reader(label_tsv, delimiter="\t"))
    return labels


DEFAULT_INSERT_COST = 1.
DEFAULT_DELETE_COST = 1.
DEFAULT_SUBSTITUTE_COST = 1.


class Error(Exception):
  """Errors specific to this module."""

  pass


class EditTransducer:
  """Factored edit transducer.
  This class stores the two factors of an finite-alphabet edit transducer and
  supports insertion, deletion, and substitution operations with user-specified
  costs.
  Note that the cost of substitution must be less than the cost of insertion
  plus the cost of deletion or no optimal path will include substitution.
  One can impose an upper bound on the number of permissible edits by
  setting a non-zero value for `bound`. This often results in substantial
  improvements in performance.
  """

  # Reserved labels for edit operations.
  DELETE = "<delete>"
  INSERT = "<insert>"
  SUBSTITUTE = "<substitute>"

  def __init__(self,
               sentence_A: str,
               sentence_B: str,
               insert_cost: float = DEFAULT_INSERT_COST,
               delete_cost: float = DEFAULT_DELETE_COST,
               substitute_cost: float = DEFAULT_SUBSTITUTE_COST,
               bound: int = 0):
    """Constructor.
    Args:
      alphabet: edit alphabet (an iterable of strings).
      insert_cost: the cost for the insertion operation.
      delete_cost: the cost for the deletion operation.
      substitute_cost: the cost for the substitution operation.
      bound: the number of permissible edits, or `0` (the default) if there
          is no upper bound.
    """
    # Left factor; note that we divide the edit costs by two because they also
    # will be incurred when traversing the right factor.
    wordlist=[]
    wordlist_A = sentence_A.split(" ")
    wordlist_B = sentence_B.split(" ")
    for word in wordlist_A:
      if word not in wordlist:
        strword = '['+ word + ']'
        wordlist.append(strword)
    for word in wordlist_B:
      if word not in wordlist:
        strword = '[' + word + ']'
        wordlist.append(strword)
    sigma = pynini.accep("")
    for word in wordlist:
      sigma = sigma.union(pynini.accep(word))
    sigma = sigma.optimize()

    insert = pynutil.insert(f"[{self.INSERT}]", weight=insert_cost / 2)
    delete = pynini.cross(
        sigma, pynini.accep(f"[{self.DELETE}]", weight=delete_cost / 2)) 
    substitute = pynini.cross(
        sigma, pynini.accep(f"[{self.SUBSTITUTE}]", weight=substitute_cost / 2)) 

    edit = pynini.union(insert, delete, substitute).optimize()
    if bound:
      sigma_star = pynini.closure(sigma)
      self._e_i = sigma_star.copy()
      for _ in range(bound):
        self._e_i.concat(edit.ques).concat(sigma_star)
    else:
      self._e_i = edit.union(sigma).closure()
  
    self._e_i.optimize()
    self._e_o = EditTransducer._right_factor(self._e_i)

  @staticmethod
  def _right_factor(ifst: pynini.Fst) -> pynini.Fst:
    """Constructs the right factor from the left factor."""
    # Ts constructed by inverting the left factor (i.e., swapping the input and
    # output labels), then swapping the insert and delete labels on what is now
    # the input side.
    ofst = pynini.invert(ifst)
    syms = pynini.generated_symbols()
    insert_label = syms.find(EditTransducer.INSERT)
    delete_label = syms.find(EditTransducer.DELETE)
    pairs = [(insert_label, delete_label), (delete_label, insert_label)]
    return ofst.relabel_pairs(ipairs=pairs)

  @staticmethod
  def check_wellformed_lattice(lattice: pynini.Fst) -> None:
    """Raises an error if the lattice is empty.
    Args:
      lattice: A lattice FST.
    Raises:
      Error: Lattice is empty.
    """
    if lattice.start() == pynini.NO_STATE_ID:
      raise Error("Lattice is empty")

  def create_lattice(self, iexpr: pynini.FstLike,
                     oexpr: pynini.FstLike) -> pynini.Fst:
    """Creates edit lattice for a pair of input/output strings or acceptors.
    Args:
      iexpr: input string or acceptor
      oexpr: output string or acceptor.
    Returns:
      A lattice FST.
    """
    iexpr = " " + iexpr + " "
    list1 = []
    sybt = dict()
    syn_list = load_labels(get_abs_path("synonym.tsv"))
    for wordlist in syn_list:
      for word in wordlist:
        str1 = " " + word + " "      
        if str1 in iexpr:# syn found
          if len(word.split(" "))>1:#syn with more than one word's
            wordstring = word.split(" ")[0]
            for j in range(1,len(word.split(" "))):
              wordstring+="_"+word.split(" ")[j]
            tagger = pynini.cross(word,wordstring)
            tagger = pynini.cdrewrite(tagger,"","",pynini.closure(utf8.VALID_UTF8_CHAR))        
            iexpr = (iexpr @ tagger).string()
    iex_list = iexpr.split(" ")
    oex_list = oexpr.split(" ")
    iex = pynini.accep("")
    oex = pynini.accep("")
    lastword = None
    for word in iex_list:
      flag = True
      if "_" in word:# show more than one word cases:
        word_more_one = word.split("_")
        word_more_one_string = word_more_one[0]       
        for j in range(1,len(word_more_one)):
          word_more_one_string+=" " + word_more_one[j]
          slist=[]
          for wordlist in syn_list:
            if word_more_one_string in wordlist:
              n = 0
              temp = pynini.accep("")
              for synword in wordlist:
                slist.append(synword)
                if len(synword.split(" "))>1:
                  ttemp = pynini.accep("")
                  synword_s = synword.split(" ")
                  for sword in synword_s:
                    idstate = pynini.accep('['+ sword + ']').paths().ilabels()[0]
                    sybt[idstate] = sword
                    ttemp+=pynini.accep('['+ sword + ']')
                  ttemp = ttemp.optimize()
                  if n==0:
                    temp=ttemp
                  else:
                    temp|=ttemp
                else:
                  idstate = pynini.accep('['+ synword + ']').paths().ilabels()[0]
                  sybt[idstate] = synword
                  if n==0:
                    temp = pynini.accep('['+ synword + ']')
                  else:
                    temp|= pynini.accep('['+ synword + ']')
                n+=1
              if len(slist)>=1:
                list1.append(slist)
              iex+=temp
      else:
        for wordlist in syn_list: 
          slist=[]
          if word in wordlist:
            temp = pynini.accep("")
            n=0
            for synword in wordlist:
                slist.append(synword)
                if len(synword.split(" "))>1:
                  ttemp = pynini.accep("")
                  synword_s = synword.split(" ")
                  for sword in synword_s:
                    idstate = pynini.accep('['+ sword + ']').paths().ilabels()[0]
                    sybt[idstate] = sword
                    ttemp+=pynini.accep('['+ sword + ']')
                  ttemp = ttemp.optimize()
                  if n==0:
                    temp=ttemp
                  else:
                    temp|=ttemp
                else:
                  idstate = pynini.accep('['+ synword + ']').paths().ilabels()[0]
                  sybt[idstate] = synword
                  if n==0:
                    temp = pynini.accep('['+ synword + ']')
                  else:
                    temp|= pynini.accep('['+ synword + ']')
                n+=1
            if len(slist)>=1:
              list1.append(slist)
            iex+=temp.optimize()
            flag = False
        if '-' in word:
          word_s = word.split('-')
          if len(word_s)==2:
            part_a = word_s[0]
            part_b = word_s[1]

            temp = (
              pynini.accep('[' + part_a + part_b + ']')  |
              pynini.accep('[' + part_a + ']') + pynini.accep('[' + part_b + ']') |
              pynini.accep('[' + word+ ']')
            )
            idstate1 = pynini.accep('[' + part_a + part_b + ']').paths().ilabels()[0]
            idstate2 = pynini.accep('[' + part_a + ']').paths().ilabels()[0]
            idstate3 = pynini.accep('[' + part_b + ']').paths().ilabels()[0]
            idstate4 = pynini.accep('[' + word+ ']').paths().ilabels()[0]
            sybt[idstate1] = part_a + part_b
            sybt[idstate2] = part_a
            sybt[idstate3] = part_b
            sybt[idstate4] = word
            iex+=temp
            flag = False
          elif len(word_s)>2:
            temp = pynini.accep("")
            for s_word in word_s:
              idstate = pynini.accep('[' + s_word + ']').paths().ilabels()[0]
              sybt[idstate] = s_word
              temp+=pynini.accep('[' + s_word + ']')
            idstate = pynini.accep('[' + word + ']').paths().ilabels()[0]
            sybt[idstate] = word
            temp = temp|pynini.accep('[' + word + ']')
            iex+=temp
            flag = False
        if flag:
            idstate = pynini.accep('[' + word + ']').paths().ilabels()[0]
            sybt[idstate] = word
            iex+=pynini.accep('['+ word + ']')
    for word in oex_list:
      flag = True
      if flag:
        idstate = pynini.accep('[' + word + ']').paths().ilabels()[0]
        sybt[idstate] = word
        oex+=pynini.accep('[' + word + ']')
    iex = iex.optimize()
    oex = oex.optimize()
    lattice = (iex @ self._e_i) @ (self._e_o @ oex)
    EditTransducer.check_wellformed_lattice(lattice)
    return list1, sybt, lattice


class LevenshteinDistance(EditTransducer):
  """Edit transducer augmented with a distance calculator."""

  def distance(self, iexpr: pynini.FstLike, oexpr: pynini.FstLike) -> float:
    """Computes minimum distance.
    This method computes, for a pair of input/output strings or acceptors, the
    minimum edit distance according to the underlying edit transducer.
    Args:
      iexpr: input string or acceptor.
      oexpr: output string or acceptor.
    Returns:
      Minimum edit distance according to the edit transducer.
    """
    list1, sybt, lattice = self.create_lattice(iexpr, oexpr)
    # The shortest cost from all final states to the start state is
    # equivalent to the cost of the shortest path.
    start = lattice.start()
    f = pynini.shortestpath(lattice, nshortest=1, unique=True)
    f = pynini.randgen(f, npath=1, select="log_prob")
    
    paths = f.paths(output_token_type="symbol")
    oexpath = paths.olabels()
    iexpath = paths.ilabels()
    spath=""
    if iexpath[0] != 0:
      spath = sybt[iexpath[0]]
    else:
      spath = ""
    for i in range(1, len(iexpath)):
      if iexpath[i]!=0:
        spath+=" " + sybt[iexpath[i]]
    error_dict = []
    d = 0
    I = 0
    s = 0
    c = 0
    for i in range(len(iexpath)):
      if iexpath[i] != oexpath[i]:
        if iexpath[i] == 0:
          error_dict.append("D")
          d += 1 
        elif oexpath[i] == 0:
          error_dict.append("I")
          I +=1
        else:
          error_dict.append("S")
          s +=1
      else:
        error_dict.append("C")
        c +=1
    count = [c,s,I,d]
    mylist = []
    if s >=0:
      for ls in list1:
        for wd in ls:
          if wd in iexpr and wd not in spath:
            tagger = pynini.cross(wd,"<"+wd +">")
            tagger = pynini.cdrewrite(tagger,"","",pynini.closure(utf8.VALID_UTF8_CHAR))        
            iexpr = (iexpr @ tagger).string()
        
    return iexpr,spath,count,error_dict, float(pynini.shortestdistance(lattice, reverse=True)[start])

