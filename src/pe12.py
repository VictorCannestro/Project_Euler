############################################################################################################################
#
# Problem 12
#
# The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
# The first ten terms would be:
#
#              1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1, 3
#  6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# 15: 1, 3, 5, 15
# 21: 1, 3, 7, 21
# 28: 1, 2, 4, 7, 14, 28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?
############################################################################################################################

import numpy as np

def genTriBruteForce(k):
    '''Generate triangle numbers i.e. the sum of first k natural numbers'''
    return sum(i for i in range(k))

def genTri(k):
    '''Generate triangle numbers via analytical formula'''
    return (k*(k+1)) // 2

def divisorsBruteForce(tri):
    '''Generate a list of the divisors of a triangle number'''
    divs = set(tri//i for i in range(1, tri//2 + 1) if tri % i == 0)
    divs.update([1, tri])
    return divs

def divisors(n):
    '''
    Args:
        n: number to get divisors of
        
    Returns:
        divisors (set): the set of divisors
        
    Notes:
        Runs in O(sqrt(n)) time
    '''
    i = 1
    divisors = set([])
    while i <= np.sqrt(n):   
        if n % i == 0:      
            if n / i == i: 
                divisors.update([i]) 
            else: 
                divisors.update([i, n//i]) 
        i += 1
    return divisors

def ndivisors(n):
    '''
    Args:
        n (int > 0): lower bound for number of divisors
    
    Returns:
        num: the value of the first triangle number to have over n divisors
    '''
    i = 1
    count = 1
    while count < n:
        i += 1
        count = len(divisors(genTri(i)))
    return genTri(i)

if __name__ == "__main__":
    n = 500
    print(ndivisors(n))

    # Answer: 76,576,500