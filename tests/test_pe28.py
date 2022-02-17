from src.pe28 import spiralDiagonals
import pytest


class TestSpiralDiagonals(object):
    ns = [3, 5]
    answers = [25, 101]
    
    @pytest.mark.parametrize("N, ans", zip(ns, answers))
    def test_given(self, N, ans):    
        calc = sum(spiralDiagonals(N))
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message
        
    def test_answer(self):
        calc = sum(spiralDiagonals(1001))
        ans = 669171001
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message