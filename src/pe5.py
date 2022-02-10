############################################################################################################################
#
# Problem 5
#
# 2520 is the smallest number that can be divided by each of 
# the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?
#
# Ans: 232792560
############################################################################################################################

def bruteForce(d: int) -> int:
    '''
    Args:
        d (int > 0): the upper bound of the consecutive divisors
    
    Returns:
        (int): the smallest positive number that is evenly divisible 
               by all of the numbers from 1 to d
    '''
    if d < 1:
        raise ValueError("Must input a positive integer.")
    elif d == 1:
        return 1
    smallest = d*(d-1)
    # A generator comprehension that checks if smallest divides the numbers 
    # from 1 to d without any remainder. Contains boolean values. 
    while sum(smallest % i == 0 for i in range(1, d+1)) != d:
        smallest += 1
    return smallest

#def smallestEvenlyDivisible(d: int) -> int:



if __name__ == "__main__":
    print(bruteForce(20))