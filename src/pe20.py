############################################################################################################################
#
# Problem 20
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is
# 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
############################################################################################################################

from functools import lru_cache

@lru_cache()
def factorial(n: int) -> int:
    '''   
    Args:
        n (int >= 0): the number to take factorial of
        
    Returns:
        (int): n!
        
    Notes: 
    
        Calculates n! recursively
        
        Uses memoization to efficiently calculate
        despite the recursive implementation.  
        
        Least Regularly Used, means that the growth 
        of the cache is limited by discarding the 
        entries that have not been read for a while.
    '''
    return 1 if n < 2 else n*factorial(n-1)

def sumDigits(x: int) -> int:
    '''Returns the sum of the digits of an integer'''
    sum_x = sum(int(i) for i in str(x))
    return sum_x

n=100
print(sumDigits(factorial(n)))
