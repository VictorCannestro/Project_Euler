import pytest
import datetime as dt
from src.pe19 import find1stSundays


def test_1():
    assert find1stSundays(dt.date(1901, 1, 1), dt.date(2000, 12, 31)) == 171