############################################################################################################################
# Lexicographic permutations
# Problem 24
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 
# 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic 
# order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
# Notes:
############################################################################################################################

from itertools import permutations

# Return successive r length permutations of elements in the iterable.
#
# The permutation tuples are emitted in lexicographic ordering according
# to the order of the input iterable. So, if the input iterable is sorted, 
# the combination tuples will be produced in sorted order.

# Elements are treated as unique based on their position, not on their 
# value. So if the input elements are unique, there will be no repeat 
# values in each permutation
calc = permutations(range(10), 10)

# Turn iterator into a list and observe the 1,000,000th value
vals = [*calc]
ans = vals[999999]

def tuple2Num(tup):
    '''
    Args:
        tup (tuple): a tuple of digits 
    Returns:
        (int): the corresponding integer
    Notes:
          >>t = (2, 7, 8, 3, 9, 1, 5, 4, 6, 0)
          >>tuple2Num(t)
              2783915460
    '''
    return sum( tup[-(i+1)] * 10**i for i in range(len(tup)) )
    
print(ans)
print(tuple2Num(ans))
