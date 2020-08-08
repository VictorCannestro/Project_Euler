#!/usr/bin/env python
# coding: utf-8

# In[1]:


# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10001st prime number?

def isPrime(num):
    '''
    Args:
        num (int): number to check if prime
    Returns:
        (bool): True if prime, false if not
    '''
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        # Check if i divides the first half of num
        for i in range(2, num//2+1):
            if num % i == 0:
                return False
        return True

def nPrimes(n):
    '''
    Args:
        n (int > 0): The index of the prime number to return
    
    Returns:
        primes (List[int]): A list of the first n primes
    '''
    i = 2 
    primes = []
    while len(primes) <= n-1:
        if isPrime(i):
            primes.append(i)
        i += 1
    return primes
        
n = 10001
print(nPrimes(n)[-1])


# In[2]:


# https://primes.utm.edu/lists/small/1000.txt
def test1():
    assert nPrimes(10)[-1] == 29

def test2():
    assert nPrimes(20)[-1] == 71

test1()
test2()

