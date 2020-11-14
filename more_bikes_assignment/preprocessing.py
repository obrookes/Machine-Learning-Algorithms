from datetime import datetime
from data_handling import *
import pandas as pd
import numpy as np

# Functions for processing timestamp data

def get_timestamp(df, index):
    '''
    Input: dataframe, row index
    Output: day and hour from corresponding timestamp as ints
    '''
    ts = df['timestamp'].iloc[index]
    date = datetime.utcfromtimestamp(ts)
    return date.day, date.hour

# Utility functions

def get_value(df, feature, index):
    '''
    Input: dataframe, feature (or column), index
    Output: value at index
    '''
    return df[feature].iloc[index]


def next_forward(df, feature, index):
    '''
    Input: dataframe, feature (or column), index of NaN value
    Output: value of the next non-null value at higher index
    '''
    for i in range(index + 1, len(df.index)):
        if(np.isnan(get_value(df, feature, i))==False):
            if(get_value(df, feature, i) is not None):
                return get_value(df, feature, i)
    raise RuntimeError(f"Error: next_forward couldnt find a non-null value")


def next_backward(df, feature, index):
    '''
    Input: dataframe, feature (or column), index of NaN value
    Output: value of the next non-null value at lower index
    '''
    for i in range((index-1), -1, -1):
        if(np.isnan(get_value(df, feature, i))==False):
            if(get_value(df, feature, i) is not None):
                return get_value(df, feature, i)
    return RuntimeError(f"Error: next_backward couldnt find a non-null value")


def next_nonnull(df, feature, index, direction):
    '''
    Input: dataframe, feature (i.e. column), index and direction (forward/backwards)
    Output: next non null feature value
    '''
    if(direction=='forward'):
        return next_forward(df, feature, index)
    elif(direction=='backward'):
        return next_backward(df, feature, index)
    else:
        raise RuntimeError(f"Error: direction must be 'forward' or 'backward'")


# Still more edge cases to deal with here...

def average_datapoints(df, feature, current_index):
    # check the nan is not the first datapoint
    if(current_index == 0):
        # if it is, take next non-null value as the nan replacement
        return next_nonnull(df, feature, current_index, direction='forward')
    # check the nan is not the final datapoint
    elif(current_index == (len(df.index)-1)):
        # if it is, take the next non-null value as the nan replacement
        return next_nonnull(df, feature, current_index, direction='backward')
    else:
        previous = next_nonnull(df, feature, current_index, 'backward')
        following = next_nonnull(df, feature, current_index, 'forward')
        return (previous + following) / 2

def clean_feature(df, feature):
    # Get list of null value locations
    null_locs = get_null_locs(df, feature)
    for index in null_locs:
        feature_value = average_datapoints(df, feature, index)
        df.at[index, feature] = feature_value
