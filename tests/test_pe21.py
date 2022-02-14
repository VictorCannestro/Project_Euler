import numpy as np
from src.pe21 import propDivisors, d, isAmicablePair, getAmicableParis, calculateSumOfAmicables
    
    
class TestD(object):
    def test_given(self):
        calc = d(284)
        ans = 220
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message        
    

class TestPropDivisors(object):
    def test_given(self):
        tol = 10e-5
        calc = propDivisors(284)
        ans = np.array([1, 2, 4, 71, 142])
        message = f"Expected {ans}\nBut got {calc}"
        assert sum(np.abs(calc - ans)) < tol, message   
 

class TestIsAmicablePair(object):
    def test_given(self):
        calc = isAmicablePair(284,220)
        ans = True
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message 

    def test_false(self):
        calc = isAmicablePair(2,3)
        ans = False
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message 
        
        
class TestGetAmicablePairs(object):
    def test_low_threshold(self):
        calc = [*getAmicableParis(10)]
        ans = []
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message 
    
    def test_smallest_pair(self):
        calc = [*getAmicableParis(300)]
        ans = [(220, 284)]
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message 
        
        
class TestCalculateSumOfAmicables(object):
    def test_answer(self):
        calc = calculateSumOfAmicables()
        ans = 31626
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message