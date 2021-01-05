from src.pe6 import squareOfSum, sumOfSquares

def test_1():
    assert squareOfSum(10) - sumOfSquares(10) == 2640
