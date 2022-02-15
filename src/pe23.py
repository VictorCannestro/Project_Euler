############################################################################################################################
# Non-abundant sums
# Problem 23
# 
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, 
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this 
# sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum 
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can 
# be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is 
# less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#
# Notes:
#        (1) The proper divisor algorithm is a bottleneck
#        (2) The sum_of_2_abundants is a bottleneck
#
# Ans: 4179871
############################################################################################################################

def propDivisors(n: int) -> list:
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
    return [x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x]

def generateAbundants(n: int) -> dict:
    '''
    Args:
        n (int): the upper bound of the search space 
    Returns:
        (dict): all the abundant numbers below the analytic limit
    Notes:
        Could use {k:sum(propDivisors(k)) for k in range(1, n+1)}
    '''
    abundants = dict()
    for key in range(1, n+1):
        calc = sum(propDivisors(key))
        if calc > key:
            abundants[key] = calc
    return abundants

def calculateNonAbundantSums(N:int=28123) -> int:
    '''
    Parameters
    ----------
    N : int, optional
        The upper limit in which all integers greater than can be written as 
        the sum of two abundant numbers. The default is 28123.
    Returns
    -------
    int
        The sum of all the positive integers which cannot be written as the 
        sum of two abundant numbers.
    '''
    abundants = generateAbundants(N)
    sum_of_2_abundants = set([i+j for i in abundants for j in abundants]) # Find all the numbers that are the sum of 2 abundant numbers (below analytic limit)
    all_nums = set([*range(1, N+1)])                                      # The set of all nums up to our analytic limit
    not_sum_of_2 = list(all_nums - sum_of_2_abundants)                    # Filter out all the numbers that can be written as the sum of two abundant numbers
    return sum(not_sum_of_2)


if __name__ == "__main__":
    print(calculateNonAbundantSums())