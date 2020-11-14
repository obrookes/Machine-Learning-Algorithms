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

def test_clean_all_features():
    data = {
            'temperature':[10, np.nan, 30, np.nan, np.nan, 40, 50],
            'rain':[1, 2, np.nan, 4, np.nan, np.nan, 7]
            }
    df = pd.DataFrame(data)

    feature_list = ['temperature', 'rain']

    clean_all_features(df, feature_list)

    # Check there are now zero NaN values for both featues in df
    assert(are_nulls(df, 'temperature')==False)
    assert(are_nulls(df, 'rain')==False)

    # Check no values modified inappropriately
    assert(get_value(df, 'temperature', 0)==10)
    assert(get_value(df, 'temperature', 5)==40)
    assert(get_value(df, 'temperature', 6)==50)

    # Check modified NaNs have been replaced with arithmetic mean
    assert(get_value(df, 'temperature', 1)==((10+30)/2))
    assert(get_value(df, 'temperature', 3)==((30+40)/2))

    # Check that NaNs immediately following modified NaN is still being calculated
    assert(get_value(df, 'temperature', 4)==((((30+40)/2) + 40)/2))
    
    # Check all the same stuff but for the second feature, 'rain'
    assert(get_value(df, 'rain', 0)==1)
    assert(get_value(df, 'rain', 1)==2)

    assert(get_value(df, 'rain', 2)==((2+4)/2))
    
    assert(get_value(df, 'rain', 4)== ((4+7)/2))
    assert(get_value(df, 'rain', 5)== ((((4+7)/2) + 7)/2))

    
def test_find_corrupt_data():
    data = {'temperature':[10, -10, 30, 75, 100, 40, 50]}
    df = pd.DataFrame(data)
    corrupt_list = find_corrupt_data(df, 'temperature', 0, 50)
    
    assert(corrupt_list.iloc[0]==False)
    assert(corrupt_list.iloc[2]==False)
    assert(corrupt_list.iloc[5]==False)
    assert(corrupt_list.iloc[1]==True)
    assert(corrupt_list.iloc[3]==True)
    assert(corrupt_list.iloc[4]==True)

def test_index_corrupt_data():
    data = {'temperature':[10, -10, 30, 0, 75, 100, 40, 50]}
    df = pd.DataFrame(data)
    corrupt_list = find_corrupt_data(df, 'temperature', 0, 50)
    corrupt_index_list = index_corrupt_data(corrupt_list)

    assert(len(corrupt_index_list)==3)
    assert(corrupt_index_list[0]==1)
    assert(corrupt_index_list[1]==4)
    assert(corrupt_index_list[2]==5)


def test_clean_holiday():
    data = {'holiday':[0, 1, np.nan, 0, np.nan]}
    df = pd.DataFrame(data)

    df['holiday'] = clean_holiday(df, 'holiday')
    assert(are_nulls(df,'holiday')==False)

    assert(df['holiday'].iloc[0]==0)
    assert(df['holiday'].iloc[1]==1)


    assert(df['holiday'].iloc[2]==0)
    assert(df['holiday'].iloc[4]==0)
