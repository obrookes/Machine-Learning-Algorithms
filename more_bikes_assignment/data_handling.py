import os
import pandas as pd
import numpy as np
from zlib import crc32
from sklearn.model_selection import StratifiedShuffleSplit


# The DataLoader class takes a csv file 
# (or a path to a csv file) as input
    
def load_data(data_file):
    return pd.read_csv(data_file)

# Random Sampling

def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

def split_data(station_data):
    station_data_indexed = station_data.reset_index()
    train_set, dev_set = split_train_test_by_id(station_data_indexed, 0.2, 'index')
    return train_set, dev_set

# Stratified Sampling

def strat_split_data(station_data):
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, dev_index in split.split(station_data, station_data["bike_category"]):
        strat_train_set = station_data.loc[train_index]
        strat_dev_set = station_data.loc[dev_index]
    return strat_train_set, strat_dev_set


# Functions to handle null values

def are_nulls(df, feature):
    return df[feature].isnull().values.any()

def count_nulls(df, feature):
    return df[feature].isnull().sum()

def get_null_locs(df, feature):
    return df[df[feature].isnull()].index.tolist()

# Functions to print null/nan information

def print_null_locs(df, feature):
    locs = get_null_locs(df, feature)
    print(locs)

def print_null_indication(df, feature):
    print('Null value: {boolean}\nNull value count: {count}'.format(
            boolean=are_nulls(df, feature),
            count=count_nulls(df, feature)))




if __name__ == "__main__":
    pass
