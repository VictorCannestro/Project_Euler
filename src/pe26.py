############################################################################################################################
#
# Problem 26
#
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 
# are given:
# 
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# 
# https://www.wikiwand.com/en/Repeating_decimal
# 
# Ans: 983
############################################################################################################################
from typing import Optional


def prime_factors(n: int) -> list:
    '''Utility function for prime decomposition'''
    i = 2
    prime_factors = []
    while i*i <= n:
        if n%i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    if n>1:
        prime_factors.append(n)
    return prime_factors

def reduced_sample_space(d_threshold:int=1000) -> list:
    '''
    Parameters
    ----------
    d_threshold : int, optional
        The largest denominator of unit fraction 1/d to consider. The default 
        is 1000.
    Returns
    -------
    list
        Of d values where those resulting terminating decimals have been 
        filtered out. A decimal is terminating if d = 2**k * 5**m for some k,m.
        Has diminishing returns as the input grows.
    '''
    return {i 
            for i in range(1, d_threshold+1) 
            if set(prime_factors(i)) not in [{2},{5},{2,5}]} - {1}
    
def calculate_digits(d: int):
    '''
    Parameters
    ----------
    d : int
        A natural number d > 0; the denominator of the unit fraction 1/d.
    Yields
    ------
    int
        The digits of  1/n. E.g. calculate_digits(8) -> [0,1,2,5]
    '''
    dividend = 1
    while dividend:      
        yield dividend // d
        dividend = dividend % d * 10
    
def calculate_cycle_length(d: int) -> int:
    '''
    Parameters
    ----------
    d : int
        A natural number d > 0; the denominator of the unit fraction 1/d.
    Returns
    -------
    int
        The length of the repetend of 1/d.
    '''
    repetend = ""
    digits = calculate_digits(d)
    next(digits)                          # Take out the initial 0
    for i, digit in enumerate(digits):    # Step though each digit
        if i == 2*(d-1):                  # It will be at most d-1. Generate extra so we can compare both sides
            break
        repetend += str(digit)
        
    L, R = repetend[:d-1], repetend[d-1:] # Split the extra in half for comparison
    while L != R:
        L, R = L[1:], R[:-1]              # Trim the edges to remove transients in the LHS
    for i in range(1, len(R)+1):
        subset = L[:i]                    # Consider the first i digits
        len_subset = len(subset)
        calc = len(L) // len_subset       # Calculate how many times the subset fits into the original
        if subset*calc == R:              # If the lengths match, we found it!
            return len_subset
    return 0
    
def find_longest_repeating(d_threshold:int=1000, sample_space:Optional=range(1,1001)) -> int:
    '''Returns the length of the longest repetend of 1/d that is found.'''
    if d_threshold == 1:
        return 0
    lengths_map = {calculate_cycle_length(d): d for d in sample_space}
    return lengths_map[max(lengths_map)]


if __name__ == '__main__':
    print(find_longest_repeating())