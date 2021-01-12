from src.pe3 import listProduct, isPrime, getPrimeFactors


def test_1():
    lst = getPrimeFactors()
    test = 600851475143
    assert listProduct(lst) == test, "The product of the factors doens't equal the input"

def test_2():
    factors = getPrimeFactors()
    assert [isPrime(i) for i in factors] == [True]*len(factors), "Not all the factors are prime"