from src.pe2 import fibSum, generateFibs, evenFibSum


class TestFibSum(object):  
    def test_typefibSum(self):
        assert type(fibSum()) == int
        
    def test_ans(self):
        assert fibSum(4000000) == 4613732
    
    
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
    


  