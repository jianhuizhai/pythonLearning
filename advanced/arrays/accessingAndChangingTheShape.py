#! /usr/bin/python3
'''
Transpose and reshape do not copy the array
'''

import numpy as np
from scipy import rand

linecomment = '='*80

M = np.identity(3)
print( np.shape(M) ) # (3, 3)

v = np.array([1., 2., 1., 4.])
print( np.shape(v) ) # (4,) <- singleton (1-tuple)

M = np.array([[1.,2.]])
print( np.shape(M) ) # (1,2)
print( M.shape )

print( np.shape(1.) )
print( np.shape([1, 2]) )
print( np.shape([[1, 2]]) )

print( linecomment )
print( '''Number of Dimensions''' )
print( linecomment )
A = rand(2,3)
print( np.ndim(A) ) # 2
print( A.ndim )

T = np.zeros((2,2,3)) # tensor of shape (2,2,3); three dimensions
print( np.ndim(T) ) # 3

print( len(np.shape(T)) ) # 3

print( linecomment )
print('''reshape''')
print( linecomment )
v = np.array([0,1,2,3,4,5])
M = v.reshape(2,3)
print( 'M = ', M )
print( np.shape(M) )
M[0,0] = 10 # now v[0] is 10
print( 'v = ', v )

v = np.array([1,2,3,4,5,6,7,8])
M = v.reshape(2,-1)
print( np.shape(M) )   # returns (2,4)

M = v.reshape(-1,2)
print( np.shape(M) )  # returns (4,2)

# M = v.reshape(3,-1) # returns error 

print( linecomment )
print('''Transpose''')
print( linecomment )
A = rand(3,4)
print( np.shape(A) ) # 3,4

B = A.T # A transpose
print( np.shape(B) ) # 4,3

v = np.array([1.,2.,3.])
print( v.T ) # exactly the same vector!
print( v.reshape(-1,1) ) # column matrix containing v
print( v.reshape(1,-1) ) # row matrix containing v

print( linecomment )
print('''Stacking''')
print( linecomment )
# v is supposed to have an even length.
def symp(v):
  n = len(v) // 2 # use the integer division //
  return np.hstack([v[-n:], -v[:n]])
v = np.arange(1,5)
print( symp(v) )