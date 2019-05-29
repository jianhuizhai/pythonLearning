#! /usr/bin/python3

import numpy as np

linecomment = '='*80

print( linecomment )
print( '''what is slow in Python''')
print( linecomment )

def my_prod(a,b):
    val = 0
    for aa,bb in zip(a,b):
        val += aa*bb
    return val

a = np.arange(3)
print( 'my_prod(a, -a) = ', my_prod(a,-a) )

print( linecomment )
print( '''vectorization''')
print( linecomment )
from scipy import empty_like

v = np.arange(1000)
w = empty_like(v)
for i in range(len(v)):
    w[i] = v[i] + 5

w = v + 5

def my_avg(A):
    m,n = A.shape
    B = A.copy()
    for i in range(1,m-1):
        for j in range(1,n-1):
            B[i,j] = (A[i-1,j] + A[i+1,j] + A[i,j-1] + A[i,j+1])/4
    return B

def slicing_avg(A):
    A[1:-1,1:-1] = (A[:-2,1:-1] + A[2:,1:-1] + A[1:-1,:-2] + A[1:-1,2:])/4
    return A

A = np.arange(20).reshape(4,-1)
print( np.allclose(my_avg(A), slicing_avg(A)) )

def my_func(x):
    y = x**3 - 2*x + 5
    if y>0.5:
        return y-0.5
    else:
        return 0

v = np.arange(10,dtype=np.float64)
for i in range(len(v)): 
    v[i] = my_func(v[i])
print( 'before vectorization' )
print( 'v = ', v )

my_vecfunc = np.vectorize(my_func)

v = np.arange(10,dtype = np.float64)
v = my_vecfunc(v)
print('after vectorization')
print( 'v = ', v )