from src.pe25 import fiboLength
import pytest


class TestFiboLength(object):
    x_digits = [1, 2, 3]
    answers = [0, 7, 12]
    
    @pytest.mark.parametrize("digits, ans", zip(x_digits, answers))
    def test_standard(self, digits, ans):
        calc = fiboLength(digits)
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message
    
    def test_answer(self):
        calc = fiboLength(1000)
        ans = 4782
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message      