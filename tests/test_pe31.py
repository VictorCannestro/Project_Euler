# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:29:19 2021

@author: Victor Cannestro
"""
import pytest
from src.pe31 import currencyCombos

@pytest.mark.skip()
def test_one():
    calc = currencyCombos(5)
    ans = 4
    message = f"Expected {ans} but got {calc}"
    assert calc == ans, message 

@pytest.mark.skip()  
def test_two():
    calc = currencyCombos(10)
    ans = 10
    message = f"Expected {ans} but got {calc}"
    assert calc == ans, message

@pytest.mark.skip()
def test_finalAns():
    calc = currencyCombos(200)
    ans = 73682
    message = f"Expected {ans} but got {calc}"
    assert calc == ans, message 