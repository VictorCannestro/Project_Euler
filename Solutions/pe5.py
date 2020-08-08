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

def test1():
    feedback = "Not the smallest number that can be divided by each of the numbers from 1 to 1 without any remainder"
    assert smallestMult(1) == 1, feedback

def test2():
    feedback = "Not the smallest number that can be divided by each of the numbers from 1 to 2 without any remainder"
    assert smallestMult(2) == 2, feedback
    
def test3():
    feedback = "Not the smallest number that can be divided by each of the numbers from 1 to 3 without any remainder"
    assert smallestMult(3) == 6, feedback
    
def test4():
    feedback = "Not the smallest number that can be divided by each of the numbers from 1 to 4 without any remainder"
    assert smallestMult(4) == 12, feedback

def test5():
    feedback = "Not the smallest number that can be divided by each of the numbers from 1 to 5 without any remainder"
    assert smallestMult(5) == 60, feedback
    
def test10():
    feedback = "Not the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder"
    assert smallestMult(10) == 2520, feedback

test1()
test2()
test3()
test4()
test5()
test10()
print(smallestMult(20))

