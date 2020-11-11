# all imports should be at the top of your script
import concurrent.futures
import os
import sys

# all function and class definitions must be next
def add(x, y):
    """Function to return the sum of the two arguments"""
    return x + y

def product(x, y):
    """Function to return the product of the two arguments"""
    return x * y

def square(x):
    """Function to return the square of the argument"""
    return x * x

r = [1, 2, 3, 4, 5]
result = map(square, r)
print(list(result))

if __name__ == "__main__":
    # You must now protect the code being run by
    # the master copy of the script by placing it
    # in this block

    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]

    # Now write your parallel code...
    etc. etc.
