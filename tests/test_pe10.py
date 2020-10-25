import pytest 
from src.pe10 import eratosthenes, sumPrime

def test_1():
    assert [*eratosthenes(20)] == [2,3,5,7,11,13,17,19]
    
def test_2():
    assert sumPrime(eratosthenes(20)) == 17+11+13+17+19
