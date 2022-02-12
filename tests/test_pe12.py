from src.pe12 import genTri, divisors, ndivisors_brute_force
import pytest


class TestGenTri(object):
    xs = range(1,8)
    answers = [1, 3, 6, 10, 15, 21, 28]
    
    @pytest.mark.parametrize("x, ans", zip(xs, answers))
    def test_standard(self, x, ans):
        calc = genTri(x)     
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message  


class TestDivisors(object):
    ns = [1, 7, 13, 25, 100]
    answers = [{1}, {1,7}, {1,13}, {1,5,25}, {1,2,4,5,10,20,25,50,100}]
    
    @pytest.mark.parametrize("n, ans", zip(ns, answers))
    def test_standard(self, n, ans):
        calc = divisors(n)     
        message = f"Expected {ans}\nBut got {calc}"
        assert divisors(n) == ans, message  


class TestNDivisorsBruteForce(object):
    ndivisors = [1, 2, 4, 5]
    answers = [1, 3, 6, 28]
    
    @pytest.mark.parametrize("n, ans", zip(ndivisors, answers))
    def test_standard(self, n, ans):
        calc = ndivisors_brute_force(n)
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message
        
    def test_answer(self):
        calc = ndivisors_brute_force(500)
        ans = 76576500
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message