from src.pe24 import digits2Num, generate_nth_permutation
import pytest


class TestGenerateNthPermutation(object):
    answers =  [(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)]
    ith = [0, 1, 2, 3, 4, 5]
    
    def test_type(self):
        assert type(generate_nth_permutation(digit_tuple=(0,1), nth=0)) == tuple
        
    @pytest.mark.xfail
    def test_not_enough_digits(self):
        with pytest.raises(ValueError) as exception_info:
            fail = generate_nth_permutation(digit_tuple=(0), nth=0)
        assert exception_info.match("Must have at least two digits in the collection")
        
    @pytest.mark.parametrize("ans, i", zip(answers, ith))
    def test_given(self, ans, i):
        calc = generate_nth_permutation(digit_tuple=(0,1,2), nth=i)
        answers = ans
        message= f"Was expecting {ans}, but got {calc}"
        assert calc == ans, message


class TestDigits2Num(object):
    def test_given(self):
        calc = digits2Num(generate_nth_permutation(digit_tuple=(0,1,2), nth=-1))
        ans = 210
        message= f"Was expecting {ans}, but got {calc}"
        assert calc == ans, message
        
    def test_type(self):
        assert type(digits2Num([0])) == int
        
    @pytest.mark.xfail
    def test_empty(self):
        with pytest.raises(ValueError) as exception_info:
            fail = digits2Num([])
        assert exception_info.match("Input must be non-empty")
        
    def test_ans(self):
        calc = digits2Num([2, 7, 8, 3, 9, 1, 5, 4, 6, 0])
        ans = 2783915460
        message= f"Was expecting {ans}, but got {calc}"
        assert calc == ans, message
        
    def test_functional(self):
        '''
        The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9
        '''
        calc = digits2Num(generate_nth_permutation((0,1,2,3,4,5,6,7,8,9), 999999))
        ans = 2783915460
        message= f"Was expecting {ans}, but got {calc}"
        assert calc == ans, message