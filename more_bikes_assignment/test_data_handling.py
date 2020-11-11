from data_handling import *
import pytest

def test_check_split():
    training_point = ['Green', 3, 'Apple']
    splitting_condition = 3
    expect = True
    test_1 = check_split(training_point, splitting_condition)
    assert(expect == test_1)

    test_2 = check_split(training_point, "Green")
    assert(expect == test_2)
    

