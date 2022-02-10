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
# Ans: 2783915460
############################################################################################################################

from itertools import permutations


def generate_nth_permutation(digit_tuple: tuple, nth: int) -> tuple:
    '''
    Parameters
    ----------
    digit_tuple : tuple
        A tuple whose length is >1 of digits in ascending order.
    nth : int
        The nth lexicographic permutation to observe.

    Returns
    -------
    list
        Return successive r length permutations of elements in the iterable.
        The permutation tuples are emitted in lexicographic ordering according
        to the order of the input iterable. So, if the input iterable is 
        sorted, the combination tuples will be produced in sorted order. Splat
        into a list then take the nth element.
    Notes:
          >>digits, nth = (0,1,2), -1
          >>generate_nth_permutation(digits, nth)
              [2,1,0]
    '''
    if len(digit_tuple) < 2:
        raise ValueError("Must have at least two digits in the collection")
    return list(permutations(digit_tuple))[nth] # Need conversion for indexing


def digits2Num(perm: tuple) -> int:
    '''
    Args:
        perm (list): a list of digits 
    Returns:
        (int): the corresponding integer with the inputted digits
    Notes:
          >>observation = (2, 7, 8, 3, 9, 1, 5, 4, 6, 0)
          >>tuple2Num(observation)
              2783915460
    '''
    digits = len(perm)
    if not digits:
        raise ValueError("Cannot pass an empty tuple.")
    return sum( perm[-(i+1)] * 10**i for i in range(digits) )

    
if __name__ == "__main__":
    # Elements are treated as unique based on their position, not on their 
    # value. So if the input elements are unique, there will be no repeat 
    # values in each permutation
    # Turn iterator into a list and observe the last value
    print(digits2Num(generate_nth_permutation((0,1), -1)))