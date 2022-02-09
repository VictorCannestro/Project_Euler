from src.pe1 import multiples


def test_type():
    assert type(multiples(n=3)) == list
    
def test_empty():
    assert sum(multiples(n=0)) == 0    

def test_simple():
    assert sum(multiples(n=6)) == 8

def test_ans():
    assert sum(multiples(n=1000)) == 233168