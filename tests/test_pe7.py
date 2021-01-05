from src.pe7 import nPrimes

# https://primes.utm.edu/lists/small/1000.txt
def test_1():
    assert nPrimes(10)[-1] == 29

def test_2():
    assert nPrimes(20)[-1] == 71
