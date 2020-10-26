import pytest 
from src.pe20 import sumDigits, factorial


def test_1():
    # 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800
    assert sumDigits(factorial(10)) == 3628800
    