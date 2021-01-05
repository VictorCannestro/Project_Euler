from src.pe5 import smallestMult

def test_1():
    feedback = "Not the smallest number that can be divided by each of the numbers from 1 to 1 without any remainder"
    assert smallestMult(1) == 1, feedback

def test_2():
    feedback = "Not the smallest number that can be divided by each of the numbers from 1 to 2 without any remainder"
    assert smallestMult(2) == 2, feedback
    
def test_3():
    feedback = "Not the smallest number that can be divided by each of the numbers from 1 to 3 without any remainder"
    assert smallestMult(3) == 6, feedback
    
def test_4():
    feedback = "Not the smallest number that can be divided by each of the numbers from 1 to 4 without any remainder"
    assert smallestMult(4) == 12, feedback

def test_5():
    feedback = "Not the smallest number that can be divided by each of the numbers from 1 to 5 without any remainder"
    assert smallestMult(5) == 60, feedback
    
def test_10():
    feedback = "Not the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder"
    assert smallestMult(10) == 2520, feedback
