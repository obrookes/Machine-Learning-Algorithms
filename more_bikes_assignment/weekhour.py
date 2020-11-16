import os
import os.path
import pandas as pd 

from data_handling import *
from preprocessing import *

path = 'Train/Train'
dir_list = os.listdir(path)

null_weekhours = 0

for f in dir_list:
    f = os.path.join(path, f)
    if(f.endswith('.csv')):
        data = load_data(f)
        if(are_nulls(data, 'weekhour')):
            null_weekhours += 1
            print(f,are_nulls(data, 'weekhour'))
        print(f,are_nulls(data, 'weekhour'))
        
assert(null_weekhours==0)
print('There are no NaN values for the weekhour feature, result!')
