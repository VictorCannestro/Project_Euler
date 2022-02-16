from src.pe27 import is_prime, eratosthenes, find_coefficients, calculate_coefficient_prod
import pytest


class TestIsPrime(object):
    nums = [1, 2, 4, 5, 8, 11]
    answers = [False, True, False, True, False, True]

    @pytest.mark.parametrize("x, ans", zip(nums, answers))
    def test_some_primes(self, x, ans):
        calc = is_prime(x)
        message = "Not all the factors are prime"
        assert calc == ans, message
    
    @pytest.mark.xfail
    def test_negative(self):
        with pytest.raises(ValueError) as exception_info: # store the exception
            calc = is_prime(-1)
        assert exception_info.match("Input must be non-negative")


class TestEratosthenes(object):
     primes_up_to = [2, 10, 20, 100] 
     answers = [{2}, 
                {2,3,5,7}, 
                {2,3,5,7,11,13,17,19}, 
                {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}]
     
     def test_edge(self):
        calc = {*eratosthenes(1)}
        ans = set()
        message = f"Expected {calc}\nBut got {ans}"
        assert calc == ans, message       
     
     @pytest.mark.parametrize("x, ans", zip(primes_up_to, answers))
     def test_standard(self, x, ans):
        calc = {*eratosthenes(x)}
        message = f"Expected {calc}\nBut got {ans}"
        assert calc == ans, message


class TestFindCoefficients(object):
    prime_map = {k:is_prime(k) for k in range(1, 10000)}

    def test_given(self):
        (a,b), length = find_coefficients(1601, self.prime_map)
        assert (a,b) == (-79, 1601)
        assert length == 80
        
    def test_answer(self):
        (a,b), length = find_coefficients(1000, self.prime_map)
        assert (a,b) == (-61, 971)
        assert length == 71


class TestFunctional(object):
    def test_answer(self):
        prime_map = {k:is_prime(k) for k in range(1, 10000)}
        info = find_coefficients(1000, prime_map)
        calc = calculate_coefficient_prod(info)
        ans = -59231
        message = f"Expected {calc}\nBut got {ans}"
        assert calc == ans, message