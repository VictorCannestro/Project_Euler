############################################################################################################################
#
# Problem 29
# https://projecteuler.net/problem=29
#
# Consider all integer combinations of a**b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:
#
# If they are then placed in numerical order, with any repeats removed, 
# we get the following sequence of 15 distinct terms:
#
# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
#
# How many distinct terms are in the sequence generated by a**b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
############################################################################################################################

import numpy as np

def powers(base, powers):
    z = np.power(base, powers)
    return z

def findCombos(a: np.array, b: np.array) -> set:
    '''
    Args:
        a (array): the bases
        b (array): the powers
    
    Returns:
        combos (set): set of Distinct powers with bases, a,
                      and powers, b
    '''
    combos = set([])
    for i in a:
        combos.update(powers(i,b))
    return combos


n = 100
a = np.arange(2,n+1)
b = np.arange(2,n+1)
combos = findCombos(a, b)

print(len(combos))
