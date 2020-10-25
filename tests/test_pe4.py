import pytest
from src.pe4 import findPalindrome

def test_1():
    assert findPalindrome(1) == 9, "Not the biggest palindrome"
    
def test_2():
    assert findPalindrome(2) == 9009, "Not the biggest palindrome"