############################################################################################################################
#
# Problem 44
#
# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum 
# and difference are pentagonal and D = |Pk − Pj| is minimised;
# what is the value of D?
# Ans: 5482660
############################################################################################################################
# import line_profiler
# %load_ext line_profiler
# %lprun -f findCandidates findCandidates(n)
# 
#Timer unit: 1e-07 s
#
#Total time: 74.7614 s
#File: <ipython-input-2-64205f537308>
#Function: findCandidates at line 16
#
#Line #      Hits         Time  Per Hit   % Time  Line Contents
#==============================================================
#    16                                           def findCandidates(n):
#    17                                               '''
#    18                                               
#    19                                               Note:
#    20                                                   k = 2167, j = 1020
#    21                                                   The value of D is 5482660
#    22                                               '''
#    23         1        252.0    252.0      0.0      x = np.arange(1,n)
#    24         1       2737.0   2737.0      0.0      Pn = p(x)
#    25         1       6749.0   6749.0      0.0      pset = set(Pn)
#    26         1         17.0     17.0      0.0      candidates = []
#    27                                           
#    28     10000      55180.0      5.5      0.0      for i in range(len(Pn)):
#    29  49995000  226390377.0      4.5     30.3          for j in range(i):
#    30  49985001  521063854.0     10.4     69.7              if Pn[i] + Pn[j] in pset:
#    31      5916      94844.0     16.0      0.0                  if Pn[i] - Pn[j] in pset:
#    32         1         23.0     23.0      0.0                      candidates.append((i, j))
#    33         1          8.0      8.0      0.0      return candidates
#
# lESSON: Seaching with 'in' seems inefficient. Perhaps using a dictionary
#         or a search algorithm will work better for future attempt
############################################################################################################################

import numpy as np


def p(x: np.array) -> np.array:
    '''Generate the xth pentagonal number'''
    return x*(3*x - 1) // 2
 
    
def findCandidates(Pn: np.array) -> list:
    '''
    Args:
        Pn (array): an array of pentagonal numbers e.g. p(np.arange(1, 10000))
        
    Returns:
        (List): the index of candidates where pk-pj and
                pj+pk are pentagonal numbers
        
    Note:
        k = 2167, j = 1020s
        The value of D is 5482660
    ''' 
    pset = set(Pn) # set for faster look-up
    candidates = []

    for k in range(len(Pn)):
        for j in range(k+1):
            if Pn[k] - Pn[j] in pset:
                if Pn[k] + Pn[j] in pset:
                    candidates.append((k, j))
    return candidates


def calculate_answer(candidates: tuple) -> int:
    k, j = candidates
    return p(k+1) - p(j+1)



if __name__ == "__main__":
    # Precompute the first n pentagonal numbers
    Pn = p(np.arange(1, 10000)) # array of 1st to nth pentagonal numbers
    print(calculate_answer(findCandidates(Pn)[0]))
