#! /usr/bin/python3

import numpy as np

linecomment = '='*80

print( linecomment )
print('''indexing with boolean arrays''')
print( linecomment )
B = np.array([[True, False],
           [False, True]])
M = np.array([[2, 3],
           [1, 4]])
print( 'M[B] = ', M[B] ) # array([2,4]), a vector

M[B] = 0
print( 'M = \n', M ) # [[0, 3], [1, 0]]

M[B] = 10, 20
print( 'M = \n', M ) # [[10, 3], [1, 20]]

M[M>2] = 0 # all the elements > 2 are replaced by 0
print( 'M = \n', M )

print( linecomment )
print( '''using where''')
print( linecomment )
def H(x):
    return np.where(x < 0, 0, 1)
x = np.linspace(-1,1,11)  # [-1. -0.8 -0.6 -0.4 -0.2 0. 0.2 0.4 0.6 0.8 1. ]
print( H(x) )            # [0 0 0 0 0 1 1 1 1 1 1]

x = np.linspace(-4,4,5)   # [-4. -2. 0. 2. 4.]
print(np.where(x > 0, np.sqrt(x), 0))  # [ 0.+0.j 0.+0.j 0.+0.j 1.41421356+0.j 2.+0.j ] 
print(np.where(x > 0, 1, -1)) # [-1 -1 -1 1 1]

a = np.arange(9)
b = a.reshape((3,3))
print( 'b = ', b )

print( np.where(a > 5)) # (array([6, 7, 8]),)

print( np.where(b > 5)) # (array([2, 2, 2]), array([0, 1, 2]))