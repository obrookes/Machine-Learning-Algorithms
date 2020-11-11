
from concurrent.futures import ProcessPoolExecutor
from functools import reduce
import urllib.request
import tarfile
import glob
import sys
import os

urllib.request.urlretrieve("https://milliams.com/courses/parallel_python/shakespeare.tar.bz2", "shakespeare.tar.bz2")
with tarfile.open("shakespeare.tar.bz2") as tar:
    tar.extractall()

def add(x, y):
    """Function to return the sum of the two arguments"""
    return x + y

def count_lines(file):
    print(f"Worker {os.getpid()}: getting lines of file")
    with open(file) as f:
        return len(f.readlines())

filenames = sorted(glob.glob(f"{sys.argv[1]}/*"))

with ProcessPoolExecutor(max_workers=10) as pool:
    line_count_iter = pool.map(count_lines, filenames)
    line_count = list(line_count_iter)

'''
reduce(arg1 = operation we want to perform, arg2 = structure we want to perform it on)
lambda (params):(operation on params) equivalent to -
    def name(arguments):
        return expression
'''

total_count = reduce(add, line_count)
print(total_count)

'''
add = lambda x, y: x + y
total_count = reduce(add, line_count)
# print(total_count)

add_10 = lambda x: add(x, 10)
# print(add_10(10))
'''