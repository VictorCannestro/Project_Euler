#!/usr/bin/env python
# coding: utf-8

# In[14]:


# 2520 is the smallest number that can be divided by each of 
# the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

def smallestMult(d):
    '''
    Args:
        d (int > 0): the upper bound of the consecutive divisors
    
    Returns:
        (int): the smallest positive number that is evenly divisible 
               by all of the numbers from 1 to d
    '''
    # Initialize the smallest
    smallest = 1
    # A generator comprehension that checks if smallest divides the numbers 
    # from 1 to d without any remainder. Contains boolean values. 
    generator = (smallest % i == 0 for i in range(1, d+1))
    
    while sum(generator) != d:
        smallest += 1
        generator = (smallest % i == 0 for i in range(1, d+1))
    return smallest

print(smallestMult(20))

