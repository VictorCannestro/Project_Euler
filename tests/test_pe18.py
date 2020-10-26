import pytest
from src.pe18 import str2Int, findPath

def test_1():
    test = '''3\n7 4\n2 4 6\n8 5 9 3'''.replace('\n',',').split(',')
    test = [row.split(' ') for row in test]
    test = str2Int(test)
    assert findPath(test) == [3,7,4,9]
  