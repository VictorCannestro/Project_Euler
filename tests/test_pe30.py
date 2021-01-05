from src.pe30 import findPowers

def test():
    n = 4
    assert sum(findPowers(n)) == 19316
