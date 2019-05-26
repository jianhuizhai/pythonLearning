#! /bin/usr/python3

import numpy as np

linecomment = '='*80

M = np.array([[1., 2.],[3.,4.]])
print( 'M[0,0] = ', M[0,0] ) # first row, first column: 1.

print( 'M[-1,0]= ', M[-1,0] ) # last row, first column: 3.

v = np.array([1., 2., 3.])
v1 = v[:2] # v1 is array([1.,2.])
print( 'v1 = ', v1 )

v1[0] = 0. # if v1 is changed ...
print( 'v1 = ', v1 )

print( 'v = ', v ) #   ... v is changed too: array([0., 2., 3.])

print( linecomment )
print( '''Altering an array using slices''')
print( linecomment )
M = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print( 'shape(M) = ', np.shape(M) )
M[1,2] = 2.0 # scalar
print( 'M = ', M )

M[2,:] = [1.,2.,3.] # vector
print( 'M = ', M )

M[1:3,:] = np.array([[1.,2.,3.],[-1.,-2.,-3.]]) # matrix
print( 'M = ',M )

M[1:4,2:3] = np.array([[1.],[0.],[-1.0]]) # column matrix
print( 'M = ', M )