import pytest
from itertools import permutations

def test_1():
    calc = [*permutations(range(3), 3)]
    ans = [(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)]
    check = [ans[i] == calc[i] for i in range(len(ans))]
    assert sum(check) == 6