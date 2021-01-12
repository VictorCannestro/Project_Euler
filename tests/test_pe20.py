from src.pe20 import sumDigits, factorial


def test_1():
    # 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800
    calc = sumDigits(factorial(10))
    ans = 3+6+2+8+8+0+0
    assert calc == ans, f"Expected {ans}\nGot {calc}"
    