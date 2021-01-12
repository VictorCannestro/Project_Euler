from src.pe18 import str2List, str2IntElements, findPath


def test_str2List():
    tri = '''3\n7 4\n2 4 6\n8 5 9 3'''
    calc = str2List(tri)
    ans = [["3"],["7","4"],["2","4","6"],["8","5","9","3"]]
    assert calc == ans, f"Expected {ans}\nGot {calc}"
    

def test_str2IntElements():
    tri = '''3\n7 4\n2 4 6\n8 5 9 3'''
    calc = str2IntElements(str2List(tri))
    ans = [[3],[7,4],[2,4,6],[8,5,9,3]]
    assert calc == ans, f"Expected {ans}\nGot {calc}"


def test_1():
    tri = '''3\n7 4\n2 4 6\n8 5 9 3'''
    test = str2IntElements(str2List(tri))
    calc = findPath(test)
    ans = [3,7,4,9]
    assert calc == ans, f"Expected {ans}\nGot {calc}"
  