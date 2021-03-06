from src.pe28 import spiralDiagonals

def test_1():
    sequences = [spiralDiagonals(N=3), spiralDiagonals(N=5)]
    ans = [sum(sequences[0]), sum(sequences[1])]
    assert ans[0] == 25
    assert ans[1] == 101
