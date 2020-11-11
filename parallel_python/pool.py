import os
import sys
from functools import reduce
from concurrent.futures import ProcessPoolExecutor

def square(x):
    """Function to return the square of the argument"""
    # print(f"Worker {os.getpid()} calculating square of {x}")
    return x * x

def cube(x):
    """Return the cube of the argument"""
    return x * x * x

if __name__ == "__main__":
    
    # create pool of workers
    # we have moved away from serial to parallel processing

    # modify no. of workers we cant for execution
    with ProcessPoolExecutor(max_workers=10) as pool:
        
        # create an array of 20 integers, from 1 to 20
        r = range(1, 21)

        squared_result = pool.map(square, r)
        cubed_result = pool.map(cube, r)
    
    # print(list(result))
    
    squared_total = reduce(lambda x, y: x + y, squared_result)
    cubed_total = reduce(lambda x, y: x + y, cubed_result)

    print(f"The sum of the square of the first 20 integers is {squared_total}")
    print(f"The sum of the cube of the first 20 integers is {cubed_total}")