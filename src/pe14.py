#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# It can be seen that a sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting 
# numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import numpy as np

def collatz(n):
    '''Generate the next number in the sequence'''
    if n % 2 ==0:
        n //= 2
    else:
        n = 3*n + 1
    return n

def lenCollatz(i):
    '''
    Args:
        i (int): the starting number of a collatz sequence
    
    Returns:
        count (int > 0): the length of the collatz sequence
    '''
    num = i
    count = 1
    # Iterate until the sequence reaches 1
    while num != 1:
        num = collatz(num)
        count += 1
    return count
   
lim = 1000000 
biggest = 1
starting = 1
for i in range(1, lim):
    length = lenCollatz(i)
    if length > biggest:
        biggest = length
        starting = i
        
print('The starting number', starting, 'achieves the longest sequence with length:', biggest)


# In[2]:


# The longest progression for any initial starting number
# less than 10**6 is 837799, which has 524 steps

def test1():
    assert collatz(13) == 40
    
def test2():
    # 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    assert lenCollatz(13) == 10
    
test1()
test2()


# In[ ]:




