import numpy as np
from src.pe21 import propDivisors, d

def test_1():
    tol = 10e-5
    calc = propDivisors(284)
    ans = np.array([1, 2, 4, 71,142])
    assert sum(np.abs(calc - ans)) < tol, f"Expected {ans}\nGot {calc}"
    
def test_2():
    calc = d(284)
    ans = 220
    assert calc == ans, f"Expected {ans}\nGot {calc}"