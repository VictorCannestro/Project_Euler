from src.pe5 import bruteForce
import pytest 


class TestSmallestMult(object):
    xs = [1, 2, 3, 4, 5, 10]
    answers = [1, 2, 6, 12, 60, 2520]
    
    def test_type(self):
        calc = type(bruteForce(1))
        ans = int
        assert calc == ans, f"Expected {ans} but got {calc}"
        
    @pytest.mark.xfail
    def test_negative(self):
        with pytest.raises(ValueError) as exception_info: # store the exception
            fail = bruteForce(-1)
        assert exception_info.match("Input must be non-negative")
    
    @pytest.mark.parametrize("x, ans", zip(xs, answers))
    def test_standard(self, x, ans):
        message = f"Not the smallest number that can be divided by each of the numbers from 1 to {x} without any remainder"
        assert bruteForce(1) == 1, message
        
    def test_ans(self):
        calc = bruteForce(20)
        ans = 232792560
        message = f"Expected {ans} but got {calc}"
        assert ans == calc, message