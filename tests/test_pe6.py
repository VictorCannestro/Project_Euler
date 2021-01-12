from src.pe6 import squareOfSum, sumOfSquares

def test_1():
    calc = squareOfSum(10) - sumOfSquares(10)
    ans = 2640
    assert calc == ans, f"Expected {ans}\nGot {calc}"
