#! /bin/usr/python3

import numpy as np

linecomment = '='*80

angle = np.pi/3
M = np.array([[np.cos(angle), -np.sin(angle)],
           [np.sin(angle), np.cos(angle)]])
v = np.array([1., 0.])
y = np.dot(M, v) 
print( 'y = ', y )

print( linecomment )
print( '''The array Type''' )
print( linecomment )

A = np.array([[1,2,3],[3,4,6]])
print( 'A.shape : ', A.shape )  # (2, 3)
print( 'A.dtype : ', A.dtype )  #  dtype('int64')
print( 'A.strides:', A.strides  )   # (24, 8)

print( linecomment )
print( '''Creating arrays from lists''' )
print( linecomment )
V = np.array([1., 2., 1.], dtype=float)
print( 'V = ', V )
V = np.array([1., 2., 1.], dtype=complex)
print( 'V = ', V )
V = np.array([1, 2]) # [1, 2] is a list of integers
print( 'V.dtype : ', V.dtype ) # int

V = np.array([1., 2]) # [1., 2] mix float/integer
print( 'V.dtype : ', V.dtype ) # float

V = np.array([1. + 0j, 2.]) # mix float/complex
print( 'V.dtype : ', V.dtype ) # complex

a = np.array([1, 2, 3])
a[0] = 0.5 
print( 'a = ', a )   # now: array([0, 2, 3])

# the identity matrix in 2D
Id = np.array([[1., 0.], [0., 1.]])
# Python allows this:
Id = np.array([[1., 0.],
            [0., 1.]])
# which is more readable