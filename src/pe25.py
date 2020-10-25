#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# The Fibonacci sequence is defined by the recurrence relation:
#
# F{n} = F{n−1} + F{n−2}, where F{1} = 1 and F{2} = 1.
# 
# The 12th term, F{12}, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence 
# to contain 1000 digits?

from functools import lru_cache

@lru_cache()
def fibo(n):
    '''Returns the nth fibonacci number'''
    if n < 2:
        return n
    return fibo(n-2) + fibo(n-1)

def fiboLength(x):
    '''
    Args:
        x (int): the desired length of the 
                 fibonacci number
    
    Return:
        (int): the index of the fibonacci 
               number of length x 
    '''
    idx = 1
    fib = 1
    while len(str(fib)) < x:
        fib = fibo(idx)
        idx += 1
    return idx

n = 1000
print(fiboLength(n))


# In[5]:


def test1():
    # The 7th term is the first term to contain two digits.
    assert fiboLength(2) == 7

def test2():
    # The 12th term is the first term to contain three digits.
    assert fiboLength(3) == 12


# In[ ]:




