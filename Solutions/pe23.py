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
############################################################################################################################

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
    return [x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x]

def sumDivisors(n):
    return sum(propDivisors(n))

def recordSums(n):
    '''
    Args:
        n (int): the upper bound of the search space 
    Returns:
        (dict): a dictionary of the natural numbers with values equal to the sum 
                of each's proper divisors
    '''
    return {k:sumDivisors(k) for k in range(1, n+1)}

# Filter to find all the abundant numbers below the analytic limit
N = 28123
abundant = [k for k,v in recordSums(N).items() if v > k]

# Find all the numbers that are the sum of 2 abundant numbers (below analytic limit) 
sum_of_2_abundants = set([i+j for i in abundant for j in abundant])

# The set of all nums up to our analytic limit 
all_nums = set([*range(1,N+1)])

# Filter out all the numbers that can be written as the sum of two abundant numbers
not_sum_of_2 = list(all_nums - x)
ans = sum(not_sum_of_2)
print(ans)