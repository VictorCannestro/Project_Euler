############################################################################################################################
# Amicable numbers
# Problem 21
# 
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
#
# Ans: 31626
############################################################################################################################
import numpy as np


def d(n):
    '''Amicable number: the sum of the proper divisors of n'''
    return np.sum(propDivisors(n))

def propDivisors(n):
    '''
    Args: 
            n (int): the number to find divisors of
    
    Notes:
            Proper divisors of n: numbers less than n which divide evenly into n
            - n != x ensures the divisor isn't the number itself
            - n % x == 0 ensures n divides x
            - range(1, (n + 1) // 2 + 1) to cut down the search space 
            
            A simplified solution suitible for small numbers
            http://rosettacode.org/wiki/Proper_divisors#Python
    '''
    return np.array([x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x])
    
def isAmicablePair(n,m):
    '''
    Amicable pair: If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and 
                   each of a and b are called amicable numbers.
    '''
    return  d(n) == m and d(m) == n

def getAmicableParis(k):
    '''Generate the amicable paris found in range [1,k]'''
    # Make a dictionary of all propor divisor sums
    candidates = {n: d(n) for n in range(1, k + 1)}
    for n, dn in candidates.items():
        # Check the conditions for an amicable pair
        if n < dn and dn <= k and candidates[dn] == n:
            yield n, dn
            

if __name__ == "__main__":
    N = 10000
    pairs = [*getAmicableParis(N)]
    result = sum(p[0]+p[1] for p in pairs)
    print(result)