from src.pe7 import nPrimes, isPrime
import pytest


class TestIsPrime(object):
    ns = [1, 2, 3, 4, 5, 81, 1000]
    answers = [False, True, True, False, True, False, False]
    
    @pytest.mark.parametrize("n, ans", zip(ns, answers))
    def test_standard(self, n, ans):
        calc = isPrime(n)
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message
    

class TestNPrime(object): 
    # https://primes.utm.edu/lists/small/1000.txt
    ns = [10, 20]
    answers = [29, 71]
    
    @pytest.mark.parametrize("n, ans", zip(ns, answers))
    def test_standard(self, n, ans):
        calc = nPrimes(n)[-1]
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message
        
    def test_answer(self):
        calc = nPrimes(10001)[-1]
        ans = 104743
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message
