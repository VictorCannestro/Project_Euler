#!/usr/bin/env python
# coding: utf-8

# In[1]:


# A palindromic number reads the same both ways. The largest palindrome made from the product 
# of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import numpy as np

def isPal(n):
    '''
    Args:
        n (int >= 0): natural number palindrome candidate
    
    Returns:
        (bool): True if palindrome, False otherwise
    '''
    # Convert each digit to an element in a list
    split = [i for i in str(n)]
    length = len(split)
    
    # Slice the first half
    a = split[:length//2]
    b = []
    
    # Is the length even or odd?
    if length % 2 == 0:
        b += split[length//2:]
    else:
        b += split[length//2 + 1:]
        
    # Reverse the second half slice
    b.reverse()
    
    # Do the two sides match exactly?
    if a == b:
        return True
    return False

def findPalindrome(d=3):
    '''
    Args:
        d (int > 0): number of digits
        
    Returns:
        largest (int): the largest palindrome made from the product of two d-digit numbers
    
    Notes:
    '''
    # Highest and lowest d-digit numbers
    h = int('9'*d)
    l = 10**(d-1)
    
    # All of the d-digit numbers row vector
    x = np.array([[*range(l,h+1)]])
    # Column vector version
    y = np.reshape(x, (len(x[0]),1))
    
    # The multiplication table of d-digit numbers
    z = y.dot(x)
    
    #  Apply the isPal function to multiplication table
    calc = np.vectorize(isPal)(z)
    
    # Filter to get palindromes pick get the biggest
    return max(z[calc])
        

def tests():
    assert findPalindrome(1) == 9, "Not the biggest palindrome"
    assert findPalindrome(2) == 9009, "Not the biggest palindrome"
    
tests()
print(findPalindrome(3))

