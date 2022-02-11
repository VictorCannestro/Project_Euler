from src.pe9 import findTriplets, product
import pytest


class TestFindTriplets(object):
    def test_given(self):
        calc = findTriplets(12)
        ans = (3,4,5)
        message =  f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
        
    @pytest.mark.xfail
    def test_empty(self):
        with pytest.raises(ValueError) as exception_info:
            fail = findTriplets(50)
        assert exception_info.match("No triplets found that sum to 50.")


class TestProduct(object):
    def test_given(self):
        calc = product((3,4,5))
        ans = 60
        message =  f"Expected {ans}\nGot {calc}"
        assert calc == ans, message  


class TestFunctional(object):
    def test_given(self):
        calc = product(findTriplets(12))
        ans = product((3,4,5))
        message =  f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
    
    def test_answer(self):
        calc = product(findTriplets(1000))
        ans = 31875000
        message =  f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
