from src.pe5 import brute_force, smallest_evenly_divisible, prime_factors_set
import pytest 


class TestPrimeFactorsSet(object):
    xs = [2, 3, 4, 10, 100]
    answers = [{2}, {3}, {2}, {2,5}, {2,5}]
    
    def test_type(self):
        calc = type(prime_factors_set(6))
        ans = set
        assert calc == ans, f"Expected {ans} but got {calc}"
        
    @pytest.mark.parametrize("x, ans", zip(xs, answers))
    def test_standard(self, x, ans):
        calc = prime_factors_set(x)
        message = f"Expected {ans} but got {calc}"
        assert calc == ans, message


class TestBruteForce(object):
    xs = [1, 2, 3, 4, 5, 10]
    answers = [1, 2, 6, 12, 60, 2520]
    
    def test_type(self):
        calc = type(brute_force(1))
        ans = int
        assert calc == ans, f"Expected {ans} but got {calc}"
        
    @pytest.mark.xfail
    def test_negative(self):
        with pytest.raises(ValueError) as exception_info: # store the exception
            fail = brute_force(-1)
        assert exception_info.match("Input must be non-negative")
    
    @pytest.mark.parametrize("x, ans", zip(xs, answers))
    def test_standard(self, x, ans):
        calc = brute_force(x)
        message = f"Expected {ans} but got {calc}"
        assert calc == ans, message
        
        
class TestSmallestMult(object):
    xs = [1, 2, 3, 4, 5, 10]
    answers = [1, 2, 6, 12, 60, 2520]
    
    def test_type(self):
        calc = type(smallest_evenly_divisible(1))
        ans = int
        assert calc == ans, f"Expected {ans} but got {calc}"
        
    @pytest.mark.xfail
    def test_negative(self):
        with pytest.raises(ValueError) as exception_info: # store the exception
            fail = smallest_evenly_divisible(-1)
        assert exception_info.match("Input must be non-negative")
    
    @pytest.mark.parametrize("x, ans", zip(xs, answers))
    def test_standard(self, x, ans):
        calc = smallest_evenly_divisible(x)
        message = f"Expected {ans} but got {calc}"
        assert calc == ans, message
        
    def test_ans(self):
        calc = smallest_evenly_divisible(20)
        ans = 232792560
        message = f"Expected {ans} but got {calc}"
        assert ans == calc, message