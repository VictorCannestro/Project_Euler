from src.pe15 import pathChoices


def test_1():
    assert pathChoices(1) == 2
    
def test_2():
    assert pathChoices(2) == 6
