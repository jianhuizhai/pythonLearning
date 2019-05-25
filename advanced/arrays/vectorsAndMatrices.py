#! /usrbin/python3

import numpy as np
from scipy.linalg import norm

linecomment = '='*80

# two vectors with three components
v1 = np.array([1., 2., 3.]) 
v2 = np.array([2, 0, 1.]) 

print('v1 = ', v1)
print('v2 = ', v2)
print( linecomment )
print('2*v1 = ', 2*v1 )
print('v1/2 = ', v1/2 )
print('3*v1 + 2*v2 = ', 3*v1+2*v2 )
print('norm(v1) = ', norm(v1) )
print('dot(v1, v2) = ', np.dot(v1, v2) )
print('dot(v1, v2) = ', v1@v2)

print( linecomment )
print('''elementwise operations''')
print( linecomment )
print('v1 * v2 = ', v1 * v2 )
print('v2 / v1 = ', v2 / v1 )
print('v2 - v1 = ', v2 - v1 )
print('v2 + v1 = ', v2 + v1 )
print('cos(v1) = ', np.cos(v1))
M = np.array( [ [1.,2], [0.,1]] )
print('M = ', M )
R = np.array( [[1.,2.,1.]] ) # notice the double brackets: this is a matrix
print('R = ', R )
print( np.shape( R ) )  # (1,3) : this is a row matrix

C = np.array( [1., 2., 1.] ).reshape(3,1)
print(' C = ', C)
print( np.shape(C) ) # this is a column matrix