from src.pe18 import str2List, str2IntElements
from src.pe18 import bottomsUp


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

      
class TestBruteForce(object):
    def test_given(self):
        calc = bottomsUp([[3],[7,4],[2,4,6],[8,5,9,3]])
        ans = sum([3,7,4,9])
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message    
            
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
        calc = bottomsUp(str2IntElements(str2List(tri)))
        ans = 1074
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message 