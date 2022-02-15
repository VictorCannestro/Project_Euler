from src.pe23 import propDivisors, generateAbundants, calculateNonAbundantSums
import pytest


class TestPropDivisors(object):
    ns = [2, 13, 100]
    answers = [[1], [1], [1,2,4,5,10,20,25,50]]
    
    def test_edge(self):
        calc = propDivisors(1)
        ans = []
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message 
        
    @pytest.mark.parametrize("n, ans", zip(ns, answers))
    def test_standard(self, n, ans):
        calc = propDivisors(n)
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message 

class TestGenerateAbundants(object):
    def test_smallest(self):
        calc = min(generateAbundants(24))
        ans = 12
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message     
        
    def test_up_to_100(self):
        calc = list(generateAbundants(100).keys())
        ans = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100]
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message
        

class TestCalculateNonAbundantSums(object):
    def test_answer(self):
        calc = calculateNonAbundantSums()
        ans = 4179871
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message