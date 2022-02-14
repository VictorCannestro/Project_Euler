from src.pe20 import sumDigits, factorial


class TestSumDigits(object):
    def test_given(self):
        # 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800
        calc = sumDigits(factorial(10))
        ans = 3+6+2+8+8+0+0
        assert calc == ans, f"Expected {ans}\nGot {calc}"
        
        
    def test_answer(self):
        calc = sumDigits(factorial(100))
        ans = 648
        assert calc == ans, f"Expected {ans}\nGot {calc}"