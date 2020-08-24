# -*- coding: utf-8 -*-
import pytest
import string
import inspect
import re
import session6
import math
import sys
import os.path

def test_TC00_01_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_TC00_02_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:  
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_TC00_02_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_TC00_03readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

from testdata_hands import vals as TD_vals, suits as TD_suits, ref_deck as TD_ref_deck
TestData_TC01=[pytest.param(session6.permutation_classic,id='permutation_classic'),
                pytest.param(session6.permutation_listcmpr,id='permutation_listcomprehension'),
                pytest.param(session6.permutation_lambda_listcmpr,id='permutation_lambda_list_comprehension')]
@pytest.mark.parametrize("Fnc",TestData_TC01)
def test_TC01_01_TestDeckCreation_(Fnc):
    TestDeck = Fnc(TD_suits,TD_vals)
    assert len(TestDeck) == 52, f"Number of cards in deck is {len(TestDeck)}"
    for Card in TD_ref_deck:
        assert Card in TestDeck,f'Card {Card} not present in deck'

from testdata_TC02 import TestData as TestData_TC02

@pytest.mark.parametrize("test_data,expected",TestData_TC02)
def test_TC02_rank_hand(test_data,expected):
    assert session6.check_hand(test_data) == expected

from testdata_TC03 import TestData as TestData_TC03
    
@pytest.mark.parametrize("hand1,hand2,expected",TestData_TC03)
def test_TC03_get_winner(hand1,hand2,expected):
    assert session6.get_winner(hand1,hand2) == expected