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
# Evaluate the sum of all the amicable numbers under 10,000.
#
# Ans: 31626. And the answer for all under 100,000 is 852810.
############################################################################################################################
import numpy as np


def d(n: int) -> int:
    '''Amicable number: the sum of the proper divisors of n'''
    return np.sum(propDivisors(n))

def propDivisors(n: int) -> np.array:
    '''
    Args: 
            n (int): the number to find divisors of
    Notes:
            Proper divisors of n: numbers less than n which divide evenly into n
            - n != x ensures the divisor isn't the number itself
            - n % x == 0 ensures n divides x
            - range(1, (n + 1) // 2 + 1) to cut down the search space 
    '''
    return np.array([x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x])
    
def isAmicablePair(n: int, m: int) -> bool:
    '''
    Amicable pair: If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and 
                   each of a and b are called amicable numbers.
    '''
    return  d(n) == m and d(m) == n

# IS A BOTTLENECK!
def getAmicableParis(k: int):
    '''Generate the amicable paris found in range [1,k]'''
    candidates = {n: d(n) for n in range(1, k + 1)}    # Make a dictionary of all propor divisor sums
    for n, dn in candidates.items():
        if n < dn and dn <= k and candidates[dn] == n: # Check the conditions for an amicable pair
            yield n, dn
            
def calculateSumOfAmicables(N:int=10000) -> int:
    return sum(p[0]+p[1] for p in getAmicableParis(N))
    
    
if __name__ == "__main__":
    print(calculateSumOfAmicables())