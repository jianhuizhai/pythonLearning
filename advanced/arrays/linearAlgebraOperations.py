#! /usr/bin/python3

import numpy as np

linecomment = '='*80

v = np.array([1.,2.])
M = np.array([[1.,2],[3.,4]])

print( 'dot(M,v) = ', np.dot(M,v) ) # matrix vector multiplication; returns a vector
print( 'dot(M,v) = ', M@v ) # alternative formulation

w = np.array([7.,0.])
print( 'dot(v,w) = ', np.dot(v,w) ) # scalar product; the result is a scalar
print( ' v @ w   = ', v@w )

N = np.array([[3., 8.],[0., 1.]])
print( 'dot(M,N) = ', np.dot(M,N) ) # results in a matrix
print( 'M @ N    = ', M @ N)

print( linecomment )
print('''Solving a linear system''')
print( linecomment )
import scipy.linalg as sl

A = np.array([[1., 2.], \
           [3., 4.]])
b = np.array([1., 4.])
x = sl.solve(A,b)
print( 'x = ', x )
print( np.allclose(np.dot(A, x), b ) )
print( np.allclose(A @ x, b) )  # alternative formulation