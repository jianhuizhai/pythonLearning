#! /usr/bin/python3

import numpy as np

linecomment = '='*80

# A = np.array([0.,0.])
# B = np.array([0.,0.])
# if abs(B-A) < 1e-10: # an exception is raised here
#     print("The two arrays are close enough")

print( linecomment )
print( '''Bool arrays''' )
print( linecomment )
A = np.array([True,False]) # Boolean array
print( 'A.dtype : ', A.dtype ) # dtype('bool')

M = np.array([[2, 3],
           [1, 4]])
print( 'M > 2 : \n', M > 2 ) # array([[False, True],
      #        [False, True]])

print( 'M == 0 : \n', M == 0 ) # array([[False, False],
       #        [False, False]])

N = np.array([[2, 3],
           [0, 0]])
print( 'M == N : \n', M == N )# array([[True, True],
       #        [False, False]])

A = np.array([[1,2],[3,4]])
B = np.array([[1,2],[3,3]])
print( 'A == B : \n', A == B ) # creates array([[True, True], [True, False]]) 
print( '(A == B).all() : ', (A == B).all() ) # False
print( '(A != B).any() : ', (A != B).any() ) # True
if (abs(B-A) < 1e-10).all():
    print("The two arrays are close enough")

print( linecomment )
print('''Checking for equality''')
print( linecomment )

data = np.random.rand(2)*1e-3
small_error = np.random.rand(2)*1e-16
data == data + small_error # False
print( 'data test1 : ', np.allclose(data, data + small_error, rtol=1.e-5, atol=1.e-8) )  # True

# The tolerance is given in terms of a relative tolerance bound, rtol , 
# and an absolute error bound, atol .
# The command allclose is a short form of: ( abs(A-B) < atol+rtol*abs(B) ).all() .

atol=1.e-6
rtol=1.e-4
print( 'A is close to B (all element) : ', (abs(A-B) < atol+rtol*abs(B)).all() )

data = 1e-3
error = 1e-16
data == data + error # False
print( 'data test2 : ', np.allclose(data, data + error, rtol=1.e-5, atol=1.e-8) )  #True