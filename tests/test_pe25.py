from src.pe25 import fiboLength

def test_1():
    # The 7th term is the first term to contain two digits.
    assert fiboLength(2) == 7

def test_2():
    # The 12th term is the first term to contain three digits.
    assert fiboLength(3) == 12
