############################################################################################################################
#
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
# 
# Ans:  142913828922
############################################################################################################################
from typing import Optional
Collection = Optional[int]


def eratosthenes(n: int) -> set:
    '''
    Args:
        n (int > 0): the upper bound of primes to consider   
    Returns:
        (generator): of prime numbers <= n
    '''
    multiples = set()                            # Use set to have unique elements
    for i in range(2, n+1):                                         
        if i not in multiples:                   # Multiples are not primes, so all leftovers are                      
            yield i                              # Yield the next prime number
            multiples.update(range(i*i, n+1, i)) # Add to the list of integer multiples: [i**2,n] in steps of i

def sum_iterable(collection: Collection) -> int:
    '''Utility function to take the sum of a collection of integers'''
    return sum(collection)


if __name__ == "__main__":
    print(sum_iterable(eratosthenes(2000000)))