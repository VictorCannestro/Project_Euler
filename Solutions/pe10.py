#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

def eratosthenes(n):
    '''
    Args:
        n (int > 0): the upper bound of primes to consider
    
    Returns:
        (generator): of prime numbers <= n
    '''
    # Use set to have unique elements
    multiples = set()
    # Iterate over each integer in interval [2,n]
    for i in range(2, n+1):
        # Multiples are not primes, so all leftovers are
        if i not in multiples:
            # Yield the next prime number
            yield i
            # Add to the list of integer multiples: [i**2,n] in steps of i 
            multiples.update(range(i*i, n+1, i))

n = 2000000
def sumPrime(primes):
    return sum(i for i in primes)

print(sumPrime([*eratosthenes(n)]))


# In[2]:


def test1():
    assert [*eratosthenes(20)] == [2,3,5,7,11,13,17,19]
    
def test2():
    assert sumPrime(eratosthenes(20)) == 17+11+13+17+19

test1()
test2()

