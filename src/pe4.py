############################################################################################################################
#
# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product 
# of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
# Ans: 906609
############################################################################################################################
import numpy as np


def is_palindrome_ver1(n: int) -> bool:
    '''
    Args:
        n (int >= 0): natural number palindrome candidate
    
    Returns:
        (bool): True if palindrome, False otherwise
    '''
    if n < 0:
        raise ValueError("Must input a natural number")
    split = [i for i in str(n)]      # Convert each digit to an element in a list
    length = len(split)
    a = split[:length//2]            # Slice the first half
    b = []
    if length % 2 == 0:              # Is the length even or odd?
        b += split[length//2:]
    else:
        b += split[length//2 + 1:]
    b.reverse()                      # Reverse the second half slice
    return a == b                    # Do the two sides match exactly?


def is_palindrome_ver2(x: int) -> bool:
    '''
    Args:
        n (int >= 0): natural number palindrome candidate
    
    Returns:
        (bool): True if palindrome, False otherwise
    '''
    if x < 0:
        raise ValueError("Must input a natural number")
    string = str(x)
    length = len(string)
    beginning, reversed_end = string[:length//2], string[::-1][length//2:]
    return string in beginning + reversed_end


def findLargestPalindrome(d=3):
    '''
    Args:
        d (int > 0): number of digits
        
    Returns:
        largest (int): the largest palindrome made from the product of two d-digit numbers
    
    Notes: This is a weird way to solve this problem.
    '''
    # Highest and lowest d-digit numbers e.g. If d=3 then h=999 and l=100
    h, l = int('9'*d), 10**(d-1)
    x = np.array([[*range(l,h+1)]])            # All of the d-digit numbers row vector
    y = np.reshape(x, (len(x[0]),1))           # Column vector version
    z = y.dot(x)                               # The multiplication table of d-digit numbers
    calc = np.vectorize(is_palindrome_ver2)(z) # Apply the isPal function to multiplication table
    return max(z[calc])                        # Filter to get palindromes pick get the biggest


if __name__ == "__main__":
    print(findLargestPalindrome(3))