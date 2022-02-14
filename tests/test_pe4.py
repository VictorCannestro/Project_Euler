from src.pe4 import findLargestPalindrome, is_palindrome_ver1, is_palindrome_ver2
import pytest


class TestIsPalindromeVer1(object):
    inputs =  [1,     15,    55,   101,  444,  100000001, 123412341234]
    answers = [True,  False, True, True, True, True,      False]
    
    @pytest.mark.xfail
    def test_nonnaturals(self):
        with pytest.raises(ValueError) as exception_info:
            calc = is_palindrome_ver1(-1)
        assert exception_info.match("Input must be non-negative")
        
    @pytest.mark.parametrize("x, ans", zip(inputs, answers))
    def test_typical_input(self, x, ans):
        calc = is_palindrome_ver1(x)
        message = "Not a palindrome"
        assert calc == ans, message


class TestIsPalindromeVer2(object):
    inputs =  [1,     15,    55,   101,  444,  100000001, 123412341234]
    answers = [True,  False, True, True, True, True,      False]
    
    @pytest.mark.xfail
    def test_nonnaturals(self):
        with pytest.raises(ValueError) as exception_info:
            fail = is_palindrome_ver2(-1)
        assert exception_info.match("Input must be non-negative")
        
    @pytest.mark.parametrize("x, ans", zip(inputs, answers))
    def test_typical_input(self, x, ans):
        calc = is_palindrome_ver2(x)
        message = "Not a palindrome"
        assert calc == ans, message


class TestFindLargestPal(object):
    def test_D1(self):
        assert findLargestPalindrome(1) == 9, "Not the biggest palindrome"
        
    def test_D2(self):
        '''
        The largest palindrome made from the product # of two 2-digit 
        numbers is 9009 = 91 × 99
        '''
        assert findLargestPalindrome(2) == 9009, "Not the biggest palindrome"
        
    def test_D3(self):
        assert findLargestPalindrome(3) == 906609, "Not the biggest palindrome"
    
