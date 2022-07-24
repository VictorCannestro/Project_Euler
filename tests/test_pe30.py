'''
REFERENCES:
https://oeis.org/A252648/internal

'''

import pytest
from src.pe30 import find_digit_sums_of_nth_powers
            
        
class TestFindDigitSumOfNthPowers(object):
    test_data = [-1, 6, "one", [1, 2]]
    
    test_expectations = [ValueError,
                         ValueError,
                         TypeError,
                         TypeError]
    
    test_ids = ["n_too_low",
                "n_too_high",
                "invalid_input_type",
                "multiple_inputs_unsupported"]
                
            
    @pytest.mark.parametrize("test_data, ex", zip(test_data, test_expectations), ids=test_ids)
    def test_invalid_partitions(self, test_data, ex):
        with pytest.raises(ex) as exception_info: 
            find_digit_sums_of_nth_powers(test_data)
        assert exception_info                   
        
    def test_third_powers(self):
        calc =  sum(find_digit_sums_of_nth_powers(3))
        ans = sum([0, 1, 153, 370, 371, 407])
        assert calc == ans, f"Expected {ans}\nBut got {calc}" 
        
    def test_given(self):
        calc = sum(find_digit_sums_of_nth_powers(4)) - 1
        ans = 19316
        assert calc == ans, f"Expected {ans}\nBut got {calc}" 
        
    def test_answer(self):
        calc = sum(find_digit_sums_of_nth_powers(5)) - 1
        ans = 443839
        assert calc == ans, f"Expected {ans}\nBut got {calc}" 
        