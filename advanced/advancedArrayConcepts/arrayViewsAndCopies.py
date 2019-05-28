#! /usr/bin/python3

import numpy as np

linecomment = '='*80

M = np.array([[1.,2.],[3.,4.]])
v = M[0,:] # first row of M
print( 'M = ', M )
print( 'v = ', v )

# The preceding slice is a view of M . It shares the same data as M . Modifying v will modify M as
# well:

v[-1] = 0.
print( 'v = ', v ) # array([[1.,0.]])
print( 'M = ', M ) # array([[1.,0.],[3.,4.]]) # M is modified as well

print( 'v.base : ', v.base ) # array([[1.,0.],[3.,4.]])

print( v.base is M ) # True
print( M.base is None )

print( linecomment )
print('''slices as views''')
print( linecomment )
a = np.arange(4) # array([0.,1.,2.,3.])
b = a[[2,3]] # the index is a list [2,3]
print( 'b = ', b ) # array([2.,3.])

print( 'b.base is None : ', b.base is None) # True, the data was copied
c = a[1:3]
print( 'c.base is None : ', c.base is None ) # False, this is just a view

N = M[:] # this is a view of the whole array M
print( 'N.base is M : ', N.base is M)

print( linecomment )
print('''Transpose and reshape as view''')
print( linecomment )
M = np.random.random_sample((3,3))
N = M.T
print( 'N.base is M : ', N.base is M )# True

v = np.arange(10)
C = v.reshape(-1,1) # column matrix
print( 'C.base is v : ', C.base is v ) # True

print( linecomment )
print( '''Array copy''' )
print( linecomment )
M = np.array([[1.,2.],[3.,4.]])
N = np.array(M.T) # copy of M.T
print( 'N.base is None : ', N.base is None )