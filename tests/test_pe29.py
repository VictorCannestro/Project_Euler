import pytest
import numpy as np
from src.pe29 import findCombos


def test_1():
    n = 5
    assert len(findCombos(np.arange(2,n+1), np.arange(2,n+1))) == 15
    