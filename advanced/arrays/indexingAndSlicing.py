#! /usr/bin/python3

import numpy as np

# works as lists

v = np.array([1.,2.,3])
M = np.array([[1.,2],[3.,4]])

print( 'v[0] = ', v[0] ) # works as for lists
print( 'v[1:]= ', v[1:])
v[0] = 10
print( 'v[0] = ', v[0] )
# slices
print( 'v[:2] = ', v[:2] )# array([10., 2.])
v[:2] = [0, 1] # now v == array([0.,1.,3.])
print( 'v = ', v )
# v[:2] = [1,2,3] # error!

print( 'M[0,0]=', M[0,0] ) # 1.
print( 'M[1:] =', M[1:] ) # matrix
print( 'M[1]  =', M[1] )  # vector