from src.pe16 import sumDigits

def test_1():
    power = 4
    n = 2**power
    assert sumDigits(n) == 7
    
def test_2():
    power = 15
    n = 2**power
    assert sumDigits(n) == 26
    