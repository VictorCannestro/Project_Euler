from src.pe14 import collatz, lenCollatz

def test_1():
    assert collatz(13) == 40
    
def test_2():
    # 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    assert lenCollatz(13) == 10
    