from src.pe15 import pathChoices


class TestPathChoices(object):
    def test_N1(self):
        calc = pathChoices(1)
        ans = 2
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
        
    def test_N2(self):
        calc = pathChoices(2)
        ans = 6
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
        
    def test_answer(self):
        calc = pathChoices(20)
        ans = 137846528820
        message = f"Expected {ans}\nGot {calc}"
        assert calc == ans, message
