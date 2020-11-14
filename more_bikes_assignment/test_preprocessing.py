from preprocessing import *
from data_handling import *
import pandas as pd
import numpy as np
import pytest

def test_next_forward():
    # Create test data
    data = {'temperature':[10, np.nan, np.nan, 40, 50]}
    df = pd.DataFrame(data)

    assert(next_forward(df, 'temperature', 3)==50)
    assert(next_forward(df, 'temperature', 0)==40)
    # Raising a runtime error if returns None value


def test_next_backward():
    # Create test data
    data = {'temperature':[10, np.nan, np.nan, 40, 50]}
    df = pd.DataFrame(data)

    assert(next_backward(df, 'temperature', 4)==40)
    assert(next_backward(df, 'temperature', 3)==10)
    assert(next_backward(df, 'temperature', 1)==10)
    # Raising a runtime error is returns None value

def test_next_nonnull():
    # Create test data
    data = {'temperature':[10, 20, 30, np.nan, np.nan, 40, 50]}
    df = pd.DataFrame(data)

    # testing going forward
    assert(next_nonnull(df, 'temperature', 0, direction='forward')==20)
    assert(next_nonnull(df, 'temperature', 2, direction='forward')==40)

    # testing going backward
    assert(next_nonnull(df, 'temperature', 6, direction='backward')==40)
    assert(next_nonnull(df, 'temperature', 5, direction='backward')==30)
    
def test_average_datapoints():
    # Create test data
    data = {'temperature':[10, 20, 30, np.nan, np.nan, 40, 50]}
    df = pd.DataFrame(data)

    assert(average_datapoints(df, 'temperature', 0)==20)
    assert(average_datapoints(df, 'temperature', 6)==40)
    assert(average_datapoints(df, 'temperature', 3)==((30+40)/2))
    assert(average_datapoints(df, 'temperature', 4)==((30+40)/2))

def test_clean_feature():
    data = {'temperature':[10, np.nan, 30, np.nan, np.nan, 40, 50]}
    df = pd.DataFrame(data)

    
    clean_feature(df, 'temperature')

    # Check there are now zero NaN values
    assert(are_nulls(df, 'temperature')==False)

    # Check no values modified inappropriately
    assert(get_value(df, 'temperature', 0)==10)
    assert(get_value(df, 'temperature', 5)==40)
    assert(get_value(df, 'temperature', 6)==50)

    # Check modified NaNs have been replaced with arithmetic mean
    assert(get_value(df, 'temperature', 1)==((10+30)/2))
    assert(get_value(df, 'temperature', 3)==((30+40)/2))

    # Check that NaNs immediately following modified NaN is still being calculated
    assert(get_value(df, 'temperature', 4)==((((30+40)/2) + 40)/2))


    


    
