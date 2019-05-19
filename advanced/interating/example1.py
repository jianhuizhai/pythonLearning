#! /usr/bin/python3

import itertools

linecomment = '=============================================================='

print( linecomment )
print('''generators''')
print( linecomment )
def odd_numbers(n):
    "generator for odd numbers less than n"
    for k in range(n):
        if k % 2 == 1:
            yield k
g = odd_numbers(22)
print( list(itertools.islice(g,22) ) )

g = odd_numbers(10)
for k in g:
    print(k,end=' ') # do something with k

for k in odd_numbers(10):
    print(k,end=' ') # do something with k

print( linecomment )
print( '''Iterators are disposable''')
print( linecomment )
L = ['a', 'b', 'c']
iterator = iter(L)
print( list(iterator) )# ['a', 'b', 'c']
print( list(iterator) )# [] empty list, because the iterator is exhausted

new_iterator = iter(L) # new iterator, ready to be used
print( list(new_iterator) )# ['a', 'b', 'c']

print( linecomment)
print('''Iterator tools''')
print( linecomment )
A = ['a', 'b', 'c']
for iteration, x in enumerate(A):
    print(iteration, x)

print( A )

A = [0, 1, 2]
for elt in reversed(A):
    print(elt)

for iteration in itertools.count():
    if iteration > 5:
        break # without this, the loop goes on forever
    print("integer {}".format(iteration))

def odd_numbers():
    k=-1
    while True:
        k+=1
        if k%2==1:
            yield k

print( list(itertools.islice(odd_numbers(),10,30,8)) )

def fibonacci(u0, u1):
    """
    Infinite generator of the Fibonacci sequence.
    """
    yield u0
    yield u1
    while True:
        u0, u1 = u1, u0+u1
        yield u1

print( list(itertools.islice(fibonacci(0, 1), 15))   )

print( linecomment )
print(  ) 
print( linecomment )
from numpy import sqrt, pi, sin
def arithmetic_geometric_mean(a, b):
    """
    Generator for the arithmetic and geometric mean
    a, b initial values
    """ 
    while True:	# infinite loop
        a, b = (a+b)/2, sqrt(a*b)
        yield a, b

from itertools import islice
def elliptic_integral(k, tolerance=1e-5, maxiter=100):
    """
    Compute an elliptic integral of the first kind.
    """
    a_0, b_0 = 1., sqrt(1-k**2)
    for a, b in islice(arithmetic_geometric_mean(a_0, b_0), maxiter):
        if abs(a-b) < tolerance:
            return pi/(2*a)
    else:
        raise Exception("Algorithm did not converge")

def pendulum_period(L, theta, g=9.81):
    return 4*sqrt(L/g)*elliptic_integral(sin(theta/2))


L=1.5
theta=pi/4
print('Period of pendulum with length {} and initial angle theta {} degree is'.format(L,theta*180/(2*pi)), \
                                                                                 pendulum_period(L,theta))