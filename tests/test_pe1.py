from src.pe1 import multiples


class TestMultiples(object):
    def test_type(self):
        assert type(multiples(n=3)) == list
        
    def test_empty(self):
        assert sum(multiples(n=0)) == 0    
    
    def test_simple(self):
        assert sum(multiples(n=6)) == 8
    
    def test_ans(self):
        assert sum(multiples(n=1000)) == 233168