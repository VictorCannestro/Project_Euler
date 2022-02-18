import numpy as np
from src.pe29 import findCombos


def test_1():
    n = 5
    assert len(findCombos(np.arange(2,n+1), np.arange(2,n+1))) == 15
    
def test_answer():
    n = 100
    a = np.arange(2, n+1)
    b = a
    calc = len(findCombos(a, b))
    ans = 9183
    message = f"Expected {ans}\nBut got {calc}"
    assert calc == ans, message