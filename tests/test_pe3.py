from src.pe3 import listProduct, isPrime, getPrimeFactors
import pytest


class TestListProd(object):
    def test_prob3(self):
        lst = getPrimeFactors()
        test = 600851475143
        message = "The product of the factors doens't equal the input"
        assert listProduct(lst) == test, message


class TestIsPrime(object):
    nums = [1, 2, 4, 5, 8, 11]
    answers = [True, True, False, True, False, True]

    @pytest.mark.parametrize("x, ans", zip(nums, answers))
    def test_some_primes(self, x, ans):
        calc = isPrime(x)
        message = "Not all the factors are prime"
        assert calc == ans, message
    
    @pytest.mark.xfail
    def test_negative(self):
        with pytest.raises(ValueError) as exception_info: # store the exception
            calc = isPrime(-1)
        assert exception_info.match("Input must be non-negative")


class TestGetPrimeFactors(object):
    def test_are_all_prime(self):
        factors = getPrimeFactors()
        calc = [isPrime(i) for i in factors]
        ans = [True]*len(factors)
        message = "Not all the factors are prime"
        assert calc == ans, message
        
    def test_given_example(self):
        calc = getPrimeFactors(13195)
        ans = [5, 7, 13, 29]
        message = "Not all the factors are the same"
        assert calc == ans, message