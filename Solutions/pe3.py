#!/usr/bin/env python
# coding: utf-8

# In[57]:


# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# Initialize variables
i = 2
factors = []
n = 600851475143
temp = n

def listProduct(nums):
    '''
    Args:
        nums (list): list of integers
    Returns:
        prod (int): product of all list elements
    '''
    prod = 1
    for i in nums:
        prod *= i
    return prod 

# Iterate until list of factors multiples to n
while listProduct(factors) != n:
    if temp % i == 0:     # If i is a factor then append
        factors.append(i)
        temp //= i        # update by dividing by i
    else:
        i += 1            # i is not a factor so check next
        
print(factors[-1])


# In[56]:


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


# In[55]:


def test1(lst):
    assert listProduct(lst) == test, "The product of the factors doens't equal the input"

def test2(lst):
    assert [isPrime(i) for i in factors] == [True]*len(factors), "Not all the factors are prime"

test1(factors)
test2(factors)

