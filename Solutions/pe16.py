#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?

power = 1000
n = 2**power

def sumDigits(n):
    '''
    Args:
        n (int): the number whose digits we'll sum
        
    Return:
        sum_digits (int): the sum of the digits of the input
    '''
    nstr= str(n)
    sum_digits = 0
    for i in nstr:
        sum_digits += int(i)
    return sum_digits
        
print(sumDigits(n))


# In[2]:


def test1():
    power = 4
    n = 2**power
    assert sumDigits(n) == 7
    
def test2():
    power = 15
    n = 2**power
    assert sumDigits(n) == 26
    
test1()
test2()


# In[ ]:




