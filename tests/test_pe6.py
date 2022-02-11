from src.pe6 import squareOfSum, sumOfSquares
import pytest


class TestSquareOfSum(object):
    '''We will use ((n * (n + 1)) // 2) ** 2'''
    xs = [1, 2, 10, 100]
    answers = [1, 3**2, 55**2, 5050**2]
    
    def test_type(self):
        calc = type(squareOfSum(1))
        ans = int
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
        
    @pytest.mark.parametrize("x, ans", zip(xs, answers))
    def test_standard(self, x, ans):
        calc = squareOfSum(x)
        assert calc == ans, f"Expected {ans}\nGot {calc}"

        
class TestSumOfSquares(object):
    xs = [1, 2, 10, 100]
    answers = [1, 5, 385, 338350]
    
    def test_type(self):
        calc = type(sumOfSquares(1))
        ans = int
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
        
    @pytest.mark.parametrize("x, ans", zip(xs, answers))
    def test_standard(self, x, ans):
        calc = sumOfSquares(x)
        assert calc == ans, f"Expected {ans}\nGot {calc}"


class TestFunctional(object):
    xs = [1, 2, 10, 100]
    answers = [1-1, 3**2-5, 55**2-385, 5050**2-338350]
    
    def test_type(self):
        calc = type(squareOfSum(1) - sumOfSquares(1))
        ans = int
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
        
    @pytest.mark.parametrize("x, ans", zip(xs, answers))
    def test_standard(self, x, ans):
        calc = squareOfSum(x) - sumOfSquares(x)
        assert calc == ans, f"Expected {ans}\nGot {calc}"
