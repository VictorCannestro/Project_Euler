from src.pe2 import brute_force, generateFibs, evenFibSum


class TestBruteForce(object):  
    def test_typefibSum(self):
        assert type(brute_force()) == int
        
    def test_ans(self):
        assert brute_force(4000000) == 4613732
    
    
class TestEvenFibSum(object): 
    def test_typeEvenFibSum(self):
        assert type(evenFibSum()) == int
        
    def test_ans(self):
        assert evenFibSum(4000000) == 4613732  
        
        
class TestGenerateFibs(object): 
    def test_typeGenerateFibs(self):
        assert str(type(generateFibs())) == "<class 'generator'>"
        
    def test_first10(self):
        assert [*generateFibs(60)] == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    


  