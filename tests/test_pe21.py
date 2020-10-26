import pytest 
import numpy as np
from src.pe21 import propDivisors, d

def test_1():
    assert propDivisors(284) == np.array([1, 2, 4, 71,142])
    
def test_2():
    assert d(284) == 220