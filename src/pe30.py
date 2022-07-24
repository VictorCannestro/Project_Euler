############################################################################################################################
#
# Problem 30
# https://projecteuler.net/problem=30
#
# Surprisingly there are only three numbers that can be written 
# as the sum of fourth powers of their digits:
#
# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4

# As 1 = 1**4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum 
# of fifth powers of their digits.
#
# Ans: 443839
############################################################################################################################

import numpy as np


def digits(x):
    '''Returns a list of the digits of x'''
    return np.array([int(i) for i in str(x)])

def find_digit_sums_of_nth_powers(n: int) -> set:
    '''
    Args:
        n (int): the power to raise to
    
    Returns:
        nth_powers (set): numbers that can be written 
                          as the sum of nth powers of 
                          their digits
    '''
    if not type(n) == int:
        raise TypeError("Function only accepts one integer as an input.")
    elif n > 5 or n < 0:
        raise ValueError("Input contains value outside of allowed bounds of [0, 5].")    
    nth_powres = set([])
    lim = 500000            # TODO: Need to programatically find the upperbound
    for i in range(0, lim): # To not include 0 or 1 in the set just set the lower range to 2
        ds = digits(i)
        if np.sum(np.power(ds, n)) == i:
            nth_powres.update([i])
    return nth_powres

if __name__ == "__main__":
    calc = find_digit_sums_of_nth_powers(3)
    print(calc)
    print(sum(calc))
