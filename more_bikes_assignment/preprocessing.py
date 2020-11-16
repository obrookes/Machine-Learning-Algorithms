from datetime import datetime
from data_handling import *
import pandas as pd
import numpy as np

################################################
''' Functions for processing timestamp data'''

def timestamp(ts):
    date = datetime.utcfromtimestamp(ts)
    return date.day, date.hour

def get_timestamp(df, index):
    '''
    Input: dataframe, row index
    Output: day and hour from corresponding timestamp as ints
    '''
    ts = df['timestamp'].iloc[index]
    return timestamp(ts)

################################################
'''Utility functions'''

def get_value(df, feature, index):
    '''
    Input: dataframe, feature name (or column), index
    Output: value at index
    '''
    return df[feature].iloc[index]

################################################
'''Functions for replacing NaNs with averages'''

def next_forward(df, feature, index):
    '''
    Input: dataframe, feature name (or column), index of NaN value
    Output: value of the next non-null value at higher index
    '''
    for i in range(index + 1, len(df.index)):
        if(np.isnan(get_value(df, feature, i))==False):
            if(get_value(df, feature, i) is not None):
                return get_value(df, feature, i)
    raise RuntimeError(f"Error: next_forward couldnt find a non-null value")


def next_backward(df, feature, index):
    '''
    Input: dataframe, feature name (or column), index of NaN value
    Output: value of the next non-null value at lower index
    '''
    for i in range((index-1), -1, -1):
        if(np.isnan(get_value(df, feature, i))==False):
            if(get_value(df, feature, i) is not None):
                return get_value(df, feature, i)
    return RuntimeError(f"Error: next_backward couldnt find a non-null value")


def next_nonnull(df, feature, index, direction):
    '''
    Input: dataframe, feature name (i.e. column), index and direction (forward/backwards)
    Output: next non null feature value
    '''
    if(direction=='forward'):
        return next_forward(df, feature, index)
    elif(direction=='backward'):
        return next_backward(df, feature, index)
    else:
        raise RuntimeError(f"Error: direction must be 'forward' or 'backward'")

def average_datapoints(df, feature, current_index):
    '''
    Input: dataframe, feature name (or column) and current row index
    Output: the average of the next available, non-null values at higher and lower indices
    '''
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
    '''
    Input: dataframe, feature name (or column)
    Output: Sets any NaN values to be average of pre- and proceeding feature values
    Note: Function does not return anything but modifies the dataframe directly
    '''
    # Get list of null value locations
    null_locs = get_null_locs(df, feature)
    for index in null_locs:
        feature_value = average_datapoints(df, feature, index)
        df.at[index, feature] = feature_value

def clean_all_features(df, feature_list):
    '''
    Input: dataframe, list of feature names (or columns)
    Output: Sets any NaN values to be average of pre- and proceeding feature values
    Note: Function does not return anything but modifies the dataframe directly
    '''
    for feature in feature_list:
        clean_feature(df, feature)

###############################################
'''Identifying Corrupt Datapoints'''

def find_corrupt_data(df, feature, minimum, maximum):
    '''
    Input: dataframe, feature, range (min and max) for the feature
    Output: dataframe with a list of boolean values 
            where True values indicate the data is corrupt
    '''
    corrupt = lambda x: x < minimum or x > maximum
    return df[feature].apply(corrupt)

def index_corrupt_data(boolean_df):
    '''
    Input: dataframe column containing boolean values
    Output: array of row indexes where boolean value is True
    '''
    return np.flatnonzero(boolean_df)

# Now we can easily write a function 
# which drops all the rows in the returned list

###############################################
'''Handling NaN holiday values '''

def clean_holiday(df, feature):
    '''
    Input: dataframe, feature name (or column)
    Output: Sets any NaN values to be average of pre- and proceeding feature values
    Note: Function does not return anything but modifies the dataframe directly
    '''
    return df[feature].fillna(0)

##############################################
''' Replacing first week of data with forward average'''

def calculate_forward_average(df, feature):
    '''
    Input: dataframe, feature name (or column)
    Output: dataframe with the values grouped by unique feature values and
            and means for all other features computed unique value computed 
    '''
    return pd.DataFrame(df.groupby([feature]).mean().reset_index())

def get_forward_average(df, weekhour, wh_value, target_var_mean):
    '''
    Input: dataframe, weekhour (feature or column heading), weekhour value (wh_value)
           target feature name (target_var_name)
    Output: The value of the mean for the target variable (for example, an average 
            of 20 bikes at weekhour 120) 
    '''
    mean = (lambda x: x == wh_value)
    boolean_df = df[weekhour].apply(mean)
    arr = np.flatnonzero(boolean_df)
    index = arr.item()
    return df[target_var_mean].iloc[index]

def apply_forward_average(df, nan_feature, weekhour):
    '''
    Input: dataframe, feature name containing NaN values, weekhour feature name
    Output: modified dataframe where all NaN values are replaced with forward averages
    '''
    null_locations = get_null_locs(df, nan_feature)
    fmean = calculate_forward_average(df, weekhour)
    for loc in null_locations:
        week_hour_value = get_value(df, weekhour, loc)
        forward_average = get_forward_average(fmean, weekhour, week_hour_value, nan_feature)
        df.at[loc, nan_feature] = forward_average






