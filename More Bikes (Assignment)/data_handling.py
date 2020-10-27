import os
import pandas as pd
import numpy as np

# The DataLoader class takes a csv file 
# (or a path to a csv file) as input

class DataLoader:
    def __init__(self, data_file):
        self._data = data_file
    
    def load_data(self):
        return pd.read_csv(self._data)

    # need to include helper function from notebook for
    # this to work properly - to do next time.

    def split_data(self, station_data, dev_percentage):
        station_data_indexed = station_data.reset_index()
        train_set, dev_set = split_train_test_by_id(station_data_indexed, 0.2, 'index')
        return train_set, dev_set



        


if __name__ == "__main__":
    pass
