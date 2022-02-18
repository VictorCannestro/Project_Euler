from src.pe30 import findPowers


class TestFindPowers(object):
    def test_given(self):
        n = 4
        assert sum(findPowers(n)) == 19316
    
    def test_answer(self):
        assert sum(findPowers(5)) == 443839