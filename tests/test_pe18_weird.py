from src.pe18_weird import str2List, str2IntElements, _list2int, _int2list, _A179477, _diffPattern
from src.pe18_weird import findPathGreedy, bruteForce
import pytest


class TestStr2List(object):
    def test_str2List(self):
        tri = '''3\n7 4\n2 4 6\n8 5 9 3'''
        calc = str2List(tri)
        ans = [["3"],["7","4"],["2","4","6"],["8","5","9","3"]]
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
    
    def test_slice(self):
        tri = '''75
    95 64
    17 47 82'''
        calc = str2List(tri)
        ans = [["75"],["95","64"],["17","47","82"]]
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
    
    
class TestStr2IntElements(object):
    def test_str2IntElements(self):
        collection = [["3"],["7","4"],["2","4","6"],["8","5","9","3"]]
        calc = str2IntElements(collection)
        ans = [[3],[7,4],[2,4,6],[8,5,9,3]]
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message


class TestList2Int(object):
    collection = [[*range(n)] for n in range(1,12)]
    answers = [0, 1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 12345678910]
    
    @pytest.mark.parametrize("lst, ans", zip(collection, answers))
    def test_standard(self, lst, ans):
        calc = _list2int(lst)
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message        
        
    def test_indices_are_2_digits(self):
        repeating = [*range(11)] + [10]
        calc = _list2int(repeating)
        ans = 1234567891010
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message


class TestInt2List(object):
    ints = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 12345678910]
    answers = [[*range(1,n+1)] for n in range(1,11)]
    
    @pytest.mark.parametrize("x, ans", zip(ints, answers))
    def test_standard(self, x, ans):
        calc = _int2list(x)
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message   
 
    def test_indices_are_2_digits(self):
        repeating = 1234567891010 
        calc = _int2list(repeating)
        ans = [*range(1,11)] + [10]
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
  

class TestA179477(object):
    ns = [-1,0,1,2,3]
    answers = [1, 10, 99, 988, 9877]
    @pytest.mark.parametrize("n, ans", zip(ns, answers))
    def test_standard(self, n, ans):
        calc = _A179477(n)
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message 
        

class TestDiffPattern(object):
    ns = [2,3,4]
    answers = [[1], [1,10,1], [1,10,1,99,1,10,1]]
    @pytest.mark.parametrize("n, ans", zip(ns, answers))
    def test_standard(self, n, ans):
        calc = _diffPattern(n)
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
        

class TestFindPathGreedy(object):
    def test_given(self):
        tri = '''3\n7 4\n2 4 6\n8 5 9 3'''
        calc = findPathGreedy(str2IntElements(str2List(tri)))
        ans = [3,7,4,9]
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message  

      
class TestBruteForce(object):
    def test_given(self):
        calc = bruteForce([[3],[7,4],[2,4,6],[8,5,9,3]])
        ans = sum([3,7,4,9])
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message    
        
    @pytest.mark.skip()      
    def test_answer(self):
        tri = '''75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
        calc = bruteForce(str2IntElements(str2List(tri)))
        ans = 1074
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message 