from src.pe14 import collatz, lenCollatz, runSimulation
import pytest 

4
class TestCollatz(object):
    xs = [13, 2, 1000000, 1000001]
    answers = [40, 1, 500000, 3000004]
    
    def test_type(self):
        assert type(collatz(1)) == int
             
    @pytest.mark.xfail
    def test_negative(self):
        with pytest.raises(ValueError) as exception_info: # store the exception
            fail = collatz(-1)
        assert exception_info.match("Input must be non-negative")

    @pytest.mark.parametrize("x, ans", zip(xs, answers))
    def test_standard(self, x, ans):
        calc = collatz(x)
        message = f"Expected {ans}, but got {calc}"
        assert calc == ans, message
    
    
class TestLenCollatz(object):
    '''https://www.wikiwand.com/en/Collatz_conjecture'''
    xs = [13, 12, 27, 2, 837799]
    answers = [9, 9, 111, 1, 524]
    
    def test_type(self):
        assert type(lenCollatz(1)) == int
    
    @pytest.mark.parametrize("x, ans", zip(xs, answers))    
    def test_standard(self, x, ans):
        #E.g.  13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
        assert lenCollatz(x) == ans
        
        
class TestRunSimulation(object): # 837799
    def test_type(self):
        assert type(runSimulation(1)) == int 
        
    def test_ans(self):
        calc = runSimulation()
        ans = 837799
        message = f"Expected {ans}, but got {calc}"
        assert ans == calc, message