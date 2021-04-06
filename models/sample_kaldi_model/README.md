* front_end FBank(dim=80)
* 40M number of params
* CNN + TDNN-F
  1. conv: 1 layer of dim 256
  2. tdnn: 15 layers of 2048-dim with 256-dim bottleneck
* LF-MMI objective_function
* NG-SGD optimizer