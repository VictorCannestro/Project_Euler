from src.pe26 import reduce_sample_space, calculate_cycle_length, find_longest_repeating
import pytest


class TestReduceSampleSpace(object):
    d_threshold = [3, 7, 17]
    answers = [[3], [3,5,6,7], [3,5,6,7,9,11,12,13,14,15,17]]
    
    @pytest.mark.parametrize("d", zip(d_threshold, answers))
    def test_magnitude(self, d, ans):
        calc = reduce_sample_space(d)
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message
        

class TestCalculateCycleLength(object):
    d_values = [1, 3, 7, 17]
    lengths = [0, 1, 6, 16]
    
    @pytest.mark.parametrize("d", d_values)
    def test_magnitude(self, d):
        calc = calculate_cycle_length(d)
        message = f"Expected {calc} < {d}\nBut got {calc < d}"
        assert (calc>=0) and (calc < d), message
    
    @pytest.mark.parametrize("d, ans", zip(d_values, lengths))
    def test_standard(self, d, ans):
        calc = calculate_cycle_length(d)
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message


class TestFunctional(object):
    d_thresholds = [1, 4, 10]
    answers = [1, 3, 7]      
    
    @pytest.mark.parametrize("d, ans", zip(d_thresholds, answers))
    def test_standard(self, d, ans):
        calc = find_longest_repeating(d)
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message
        
    def test_answer(self):
        calc = find_longest_repeating(d_threshold=1000)
        ans = 983
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message