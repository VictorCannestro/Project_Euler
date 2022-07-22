import pytest
from src.pe29 import generate_combinations, number_of_distinct_terms


class TestNumberOfDistinctTerms(object):
    test_data = [[(1, 5), (2, 5)],
                 [(2, 101), (2, 5)],
                 [(2, 5), (-1, 5)],
                 [(2, 5), (2, 101)],
                 [("one", "two"), (2, 5)],
                 [(5), (2,5)]]
    
    test_expectations = [ValueError,
                         ValueError,
                         ValueError,
                         ValueError,
                         TypeError,
                         TypeError]
    
    test_ids = ["test_a_not_too_small",
                "test_a_not_too_large",
                "test_b_not_too_small",
                "test_b_not_too_large",
                "test_only_accept_integer_lists",
                "test_insufficient_args"]
               
    
    def test_given(self):
        a_range, b_range = (2, 5), (2, 5)
        combinations = generate_combinations(a_range, b_range)
        calc = number_of_distinct_terms(combinations)
        ans = 15
        assert calc == ans, f"Expected {ans}\nBut got {calc}"  
       
    @pytest.mark.parametrize("test_data, ex", zip(test_data, test_expectations), ids=test_ids)
    def test_invalid_partitions(self, test_data, ex):
        a_range, b_range = test_data
        with pytest.raises(ex) as exception_info: 
            generate_combinations(a_range, b_range)
        assert exception_info                   
        
    def test_answer(self):
        a_range, b_range = (2, 100), (2, 100)
        combinations = generate_combinations(a_range, b_range)
        calc = number_of_distinct_terms(combinations)
        ans = 9183
        assert calc == ans, f"Expected {ans}\nBut got {calc}" 