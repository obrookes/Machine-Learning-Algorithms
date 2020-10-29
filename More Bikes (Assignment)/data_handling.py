import os
import pandas as pd
import numpy as np
from zlib import crc32


# The DataLoader class takes a csv file 
# (or a path to a csv file) as input
    
def load_data(data_file):
    return pd.read_csv(data_file)

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


if __name__ == "__main__":
    pass
