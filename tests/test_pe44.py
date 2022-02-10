from src.pe44 import findCandidates, p, calculate_answer
import numpy as np
import pytest


class TestP(object):    
    def test_standard_vals(self):
        ans = np.asarray([1, 5, 12, 22, 35, 51, 70, 92, 117, 145])
        xs = np.arange(1,11)
        calc = p(xs)
        check = [xs[i] == ans[i] for i in range(0,10)]
        message = f"Expected {ans}, but got {calc}"
        assert sum(check) == len(ans), message 
        

class TestFindCandidates(object):
    def test_functional(self):
        calc = findCandidates(p(np.arange(1, 10000)))
        ans = [(2166, 1019)]
        message = f"Expected {ans}, but got {calc}"
        assert calc == ans, message 
        
        
class TestCalculateAns(object):
    def test_type(self):
        ans = int
        calc = type(calculate_answer((2166, 1019)))
        message = f"Expected {ans}, but got {calc}"
        assert calc == ans, message 
        
    def test_ans(self):
        calc = calculate_answer((2166, 1019))
        ans = 5482660
        message = f"Expected {ans}, but got {calc}"
        assert calc == ans, message 
        
    def test_functional(self):
        Pn = p(np.arange(1, 10000))
        calc = calculate_answer(findCandidates(Pn)[0])
        ans = 5482660
        message = f"Expected {ans}, but got {calc}"
        assert calc == ans, message 