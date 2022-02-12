from src.pe10 import eratosthenes, sum_iterable
import pytest


class TestEratosthenes(object):
     primes_up_to = [2, 10, 20, 100] 
     answers = [{2}, 
                {2,3,5,7}, 
                {2,3,5,7,11,13,17,19}, 
                {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}]
     
     def test_edge(self):
        calc = {*eratosthenes(1)}
        ans = set()
        message = f"Expected {calc}\nBut got {ans}"
        assert calc == ans, message       
     
     @pytest.mark.parametrize("x, ans", zip(primes_up_to, answers))
     def test_standard(self, x, ans):
        calc = {*eratosthenes(x)}
        message = f"Expected {calc}\nBut got {ans}"
        assert calc == ans, message
    
    
class TestSumIterable(object):
     collections = [{2}, [1,2], range(0,3)] 
     answers = [2, 3, 3]
                
     @pytest.mark.xfail
     def test_wrong_type(self):
        with pytest.raises(TypeError) as exception_info:
            fail = sum_iterable(['2', '3', '5'])
        assert exception_info.match("Input must be a collection of ints")

     @pytest.mark.parametrize("collection, ans", zip(collections, answers))
     def test_collections(self, collection, ans):
        calc = sum_iterable(collection)
        message = f"Expected {calc}\nBut got {ans}"
        assert calc == ans, message
    
     def test_20(self):
        calc = sum_iterable(eratosthenes(20))
        ans = sum_iterable(eratosthenes(10)) + 11 + 13 + 17 + 19
        message = f"Expected {calc}\nBut got {ans}"
        assert calc == ans, message


class TestFunctional(object):
    def test_10(self):
        calc = sum_iterable(eratosthenes(10))
        ans = 2 + 3 + 5 + 7
        message = f"Expected {calc}\nBut got {ans}"
        assert calc == ans, message
        
    def test_20(self):
        calc = sum_iterable(eratosthenes(20))
        ans = sum_iterable(eratosthenes(10)) + 11 + 13 + 17 + 19
        message = f"Expected {calc}\nBut got {ans}"
        assert calc == ans, message
        
    def test_answer(self):
        calc = sum_iterable(eratosthenes(2000000))
        ans = 142913828922
        message = f"Expected {calc}\nBut got {ans}"
        assert calc == ans, message 