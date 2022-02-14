import datetime as dt
from src.pe19 import find1stSundays


class TestFind1stSundays(object):
    def test_answer(self):
        calc = find1stSundays(dt.date(1901, 1, 1), dt.date(2000, 12, 31))
        ans = 171
        message = f"Expected {ans}\nBut got {calc}"
        assert calc == ans, message 