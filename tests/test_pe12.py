import pytest
from src.pe12 import genTri, divisors, ndivisors

def test_1():
    assert divisors(genTri(5)) == set([1, 3, 5, 15])
    
def test_2():
    assert ndivisors(4) == 6
    