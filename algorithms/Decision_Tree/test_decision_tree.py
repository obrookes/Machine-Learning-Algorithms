from decision_tree import *
import pytest

def test_check_split():
    training_point = ['Green', 3, 'Apple']
    splitting_condition = 3
    expect = True
    test_1 = check_split(training_point, splitting_condition)
    assert(expect == test_1)

    test_2 = check_split(training_point, "Green")
    assert(expect == test_2)

def test_partition():

    training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
    ]

    splitting_condition = 3
    true, false = partition(training_data, splitting_condition)
    assert(len(true) == 3)
    assert(len(false) == 2)

def test_get_class_freq():

    training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
    ]

    class_freq = get_class_freq(training_data)
    assert(class_freq['Apple'] == 2)
    assert(class_freq['Grape'] == 2)
    assert(class_freq['Lemon'] == 1)

def test_gini():

    training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
    ]

    

