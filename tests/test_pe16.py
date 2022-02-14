from src.pe16 import sum_digits
import pytest


class TestSumDigits(object):
    powers = [4, 15]
    answers = [7, 26]
    
    @pytest.mark.parametrize("power, ans", zip(powers, answers))
    def test_standard(self, power, ans):
        calc = sum_digits(2**power)
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message   
        
    def test_answer(self):
        calc = sum_digits(2**1000) 
        ans = 1366
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message
    