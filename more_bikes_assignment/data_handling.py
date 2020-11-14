import os
import pandas as pd
import numpy as np
from zlib import crc32
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer


# The DataLoader (would-be) class takes a csv file 
# (or a path to a csv file) as input
    
def load_data(data_file):
    return pd.read_csv(data_file)

# Display functions
# DIsplay train test distribution

def display_train_test_dist(train, dev, feature, target):
    fig, ax = plt.subplots()
    train.plot.scatter(feature, target, color="red", marker="o", ax=ax, label="train")
    dev.plot.scatter(feature, target, color="blue", marker="x", ax=ax, label="development")
    ax.legend();

def scatter_plot(df, feature, target):
    df.plot.scatter(feature, target);

def histogram(df, feature):
    df[feature].hist()

# Display dimensions and length of train and dev sets

def display_shapes(train_df, dev_df):
    print('Train: {train}\nDev: {dev}'.format(
            train=train_df.shape,
            dev=dev_df.shape))

# Functions to print null/nan information

def print_null_locs(df, feature):
    print('Null locations:\n{locs}'.format(
            locs=get_null_locs(df, feature)))

def print_null_indication(df, feature):
    print('Null value: {boolean}\nNull value count: {count}'.format(
            boolean=are_nulls(df, feature),
            count=count_nulls(df, feature)))

# Functions to handle null values

def are_nulls(df, feature):
    return df[feature].isnull().values.any()

def count_nulls(df, feature):
    return df[feature].isnull().sum()

def get_null_locs(df, feature):
    return df[df[feature].isnull()].index.tolist()

# Need to convert to a class...
# Functions to handle missing values

def simple_imputer(df, feature, strategy):
    imputer = SimpleImputer(strategy=strategy)
    imputer.fit(df[[feature]])
    transformed_feature = imputer.transform(df[[feature]])
    return pd.DataFrame(transformed_feature, columns=df.columns)

# need a method to call imputer.statistics_ etc.

