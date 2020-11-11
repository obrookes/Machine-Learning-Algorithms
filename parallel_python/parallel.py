import math

def add(x, y):
    """Simple function returns the sum of the arguments"""
    return x + y

def multiply(x, y):
    """
    Simple function that returns the product of the
    two arguments
    """
    return x * y

def mapper(func, arg1, arg2):
    """
    This will map the function 'func' to each pair
    of arguments in the list 'arg1' and 'arg2', returning
    the result
    """
    res = []

    for i, j in zip(arg1, arg2):
        r = func(i, j)
        res.append(r)

    return res

def calc_distance(point1, point2):
    """
    Function to calculate and return the distance between
    two points
    """
    dx2 = (point1[0] - point2[0]) ** 2
    dy2 = (point1[1] - point2[1]) ** 2
    dz2 = (point1[2] - point2[2]) ** 2

    return math.sqrt(dx2 + dy2 + dz2)

'''
Instead, the built-in map function has returned an object which is ready 
and waiting to perform the calculation you’ve asked, but won't actually 
run those calculations unitl you request the result. This can be useful 
because by evaluating the map “lazily”, you can avoid unnecessary computation. 
The technical term for the thing that has been returned is an iterator.

If you want to force Python to evaluate the map and 
give you the answers, you can turn it into a list 
using the list function.
'''

def make_iterator(func, arg1, arg2):
    return map(func, arg1, arg2)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

def square(x):
    """
    Simple function to return the square of
    the passed argument
    """
    return x * x

numbers = [1, 2, 3, 4, 5]

result = map(square, numbers)
result_list = list(result)




