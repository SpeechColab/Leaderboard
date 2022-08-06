from typing import Iterable, List

import pynini
from pynini.lib import pynutil#, utf8

# REFERENCE: https://github.com/kylebgorman/pynini/blob/master/pynini/lib/edit_transducer.py
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
               alphabet: Iterable[str],
               insert_cost: float = 1.0,
               delete_cost: float = 1.0,
               substitute_cost: float = 1.0,
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
    sigma = pynini.union(*alphabet).optimize()
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
    lattice = (iexpr @ self._e_i) @ (self._e_o @ oexpr)
    EditTransducer.check_wellformed_lattice(lattice)
    return lattice


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
    lattice = self.create_lattice(iexpr, oexpr)
    # The shortest cost from all final states to the start state is
    # equivalent to the cost of the shortest path.
    start = lattice.start()
    return float(pynini.shortestdistance(lattice, reverse=True)[start])
  
  # Jiayu
  def compute_alignment(self, iexpr: pynini.FstLike, oexpr: pynini.FstLike) -> pynini.FstLike:
    lattice = self.create_lattice(iexpr, oexpr)
    alignment = pynini.shortestpath(lattice, nshortest=1, unique=True).optimize()
    return alignment


def print_symbol_table(symbol_table):
  print('SYMTAB:')
  for k in range(symbol_table.num_symbols()):
    sym = symbol_table.find(k)
    assert(symbol_table.find(sym) == k) # symbol table's find can be used for bi-directional lookup (id <-> sym)
    print(k, sym)
  print()

def compute_token_error_rate(c, s, i, d):
  return 100.0 * (s + d + i) / (s + d + c)

def make_symbol_table(vocabulary):
  symbol_table = pynini.SymbolTable()
  for x in ['<epsilon>'] + vocabulary:
    symbol_table.add_symbol(x)
  #symbol_table.write_text('symbol_table.txt')
  return symbol_table

if __name__ == '__main__':
  print('-' * 15, 'INPUT', '-' * 15)

  ref_text = "I'M JAY"
  hyp_text = "I AM JAY"

  ref_tokens = ref_text.strip().split()
  print('REF TEXT:', ref_text)
  print('REF TOKENS:', ref_tokens)

  hyp_tokens = hyp_text.strip().split()
  print('HYP TEXT:', hyp_text)
  print('HYP TOKENS:', hyp_tokens)

  print()

  #print('-' * 15, 'WER', '-' * 15)
  #vocab = list(set(ref_tokens + hyp_tokens))
  #print('VOCABULARY:', vocab)

  #symtab = make_symbol_table(vocab)
  #print_symbol_table(symtab)

  #ref_fst = pynini.accep(ref_text, token_type = symtab)
  #print('REF FST:', ref_fst.string(token_type = symtab))
  #print(ref_fst)

  #hyp_fst = pynini.accep(hyp_text, token_type = symtab)
  #print('HYP FST:', hyp_fst.string(token_type = symtab))
  #print(hyp_fst)


  #ld_computer = LevenshteinDistance(alphabet = [ pynini.accep(token, token_type = symtab) for token in vocab ])
  #d = ld_computer.distance(iexpr = ref_fst, oexpr = hyp_fst)
  #print(f'DISTANCE(RAW): {d}')
  #print()

  print('-' * 15, 'WER with synonyms', '-' * 15)
  syn_sets = {
    '<SYN001>' : ["I'M", 'I AM'],
    '<SYN002>' : ['T-SHIRT', 'T SHIRT', 'TSHIRT'],
  }

  syn_tokens = []
  for syn_name, syn_set in syn_sets.items():
    for phrase in syn_set:
      syn_tokens += phrase.split()

  vocab = list(set(ref_tokens + hyp_tokens + syn_tokens))
  print('VOCABULARY:', vocab)

  symtab = make_symbol_table(vocab)
  print_symbol_table(symtab)

  SYN001_slot = pynini.union(
    pynini.accep("I'M", token_type = symtab),
    pynini.accep('I AM', token_type = symtab),
  )

  ref_fst = pynini.accep(ref_text, token_type = symtab)
  print('REF FST(SYN):')
  print(ref_fst)

  hyp_fst = (SYN001_slot + pynini.accep('JAY', token_type = symtab)).optimize()
  print('HYP FST(SYN):')
  print(hyp_fst)

  ld_computer = LevenshteinDistance(alphabet = [ pynini.accep(token, token_type = symtab) for token in vocab ])
  alignment = ld_computer.compute_alignment(iexpr = ref_fst, oexpr = hyp_fst)
  print('ALIGNMENT:')
  print(alignment)


  C, S, I, D = 0, 0, 0, 0
  for state in alignment.states():
    for arc in alignment.arcs(state):
      i, o = arc.ilabel, arc.olabel
      print(i, o)

      if i != 0 and o != 0 and i != o:
        S += 1
      elif i != 0 and o == 0:
        D += 1
      elif i == 0 and o != 0:
        I += 1
      elif i == o:
        C += 1
      else:
        raise RuntimeError

  token_error_rate = compute_token_error_rate(C, S, I, D)
  print('TER:', token_error_rate)
