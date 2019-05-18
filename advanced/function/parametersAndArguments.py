#! /usr/bin/python3

linecomment = '==================================================================='
# Passing arguments – by position and by keyword

def subtract( x1, x2):
    return x1 - x2

print( subtract(5.0, 4.3) )
z = 3
e = subtract(5, z)
print( e )
e = subtract(x2 = z, x1 = 5)
print( e )

print(linecomment)
print('''Changing argument''')
print( linecomment )
# This applies to all immutable arguments, such as strings, numbers and tuples
# The situation is different if mutable arguments, such as lists or dictionaries, are changed.
def subtract(x1, x2):
    z = x1 - x2
    x2 = 50.
    return z

a = 20.
b = subtract(10, a)

print( 'a = {}'.format( a ) )

# this is not recommand. The value of input paramters are changed in function
def subtract(x):
    z = x[0] - x[1]
    x[1] = 50.
    return z

a = [10, 20]
b = subtract(a)
print('a = {}'.format( a ) )

print( linecomment )
print('''Access to variables defined outside the local namespace''')
print( linecomment )

import numpy as np
def sqrt(x):
    return np.sqrt(x)
a = 3
def multiply(x):
    return a * x # bad style: access to the variable a defined outside

def multiply(x, a):
    return a * x

print( linecomment )
print('''Default arguments''')
print( linecomment )

def subtract(x1, x2 = 0):  # default value of x2 is 0.
    return x1 - x2

print( subtract( 10 ) )
print( subtract(10, 2) ) 

print( linecomment )
print( '''Variable number of arguments''')
print( linecomment )

import matplotlib.pyplot as plt

data = [[1,2],[3,4]]
style = dict({'linewidth':3,'marker':'o','color':'green'})
# Then we can call the plot function using starred ( * ) arguments:
plt.plot(*data,**style)
plt.show()

print( linecomment )
print( '''Return values''')
print( linecomment )

def complex_to_polar(z):
    from scipy import arctan2
    r = sqrt(z.real ** 2 + z.imag ** 2)
    phi = arctan2(z.imag, z.real)
    return (r,phi) # here the return object is formed

z = 3 + 5j  # here we define a complex number
a = complex_to_polar(z)
r = a[0]
phi = a[1]

# The last three statements can be written more elegantly in a single line
r,phi = complex_to_polar(z)

print( linecomment )
print( '''Recursive function''')
print( linecomment )
def chebyshev(n, x):
    if n == 0:
        return 1.
    elif n == 1:
        return x
    else:
        return 2. * x * chebyshev(n - 1, x) \
                      - chebyshev(n - 2 ,x)

a = chebyshev(5, 0.52) # returns 0.39616645119999994
print( a )

print( linecomment )
print('''Function documentation''')
print( linecomment )
def newton(f, x0):
    """
    Newton's method for computing a zero of a function
    on input:
    f (function) given function f(x)
    x0 (float) initial guess
    on return:
    y (float) the approximated zero of f
    """
print(help(newton))
print( linecomment )
print('''Functions are objects''')
print( linecomment )
def square(x):
    """
    Return the square of x
    """
    return x ** 2
print( square(4) )# 16
sq = square # now sq is the same as square
print( sq(4) ) # 16
del square # square doesn't exist anymore
print(newton(sq, .2)) # passing as argument

print(linecomment)
print('''Partial application''' )
print( linecomment )
def sin_omega(t, freq):
    from numpy import sin, pi
    return sin(2 * pi * freq * t)
def make_sine(freq):
    "Make a sine function with frequency freq"
    def mysine(t):
        return sin_omega(t, freq)
    return mysine
sin1=make_sine(1)
print( sin1(2) )

print( linecomment )
print('''Anonymous functions – the lambda keyword''')
print( linecomment )
