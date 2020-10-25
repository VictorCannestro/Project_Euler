import pytest
from src.pe9 import findTriplets, product


def test_1():
    assert findTriplets(12) == (3,4,5)
    
def test_2():
    assert product(findTriplets(12)) == 3*4*5
