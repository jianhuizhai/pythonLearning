#! /usr/bin/python3

import numpy as np

linecomment = '='*80

print( linecomment )
print( '''mathematical view''')
print( linecomment )
vector = np.arange(4) # array([0.,1.,2.,3.])
print( 'vector + 1 = ', vector + 1)  # array([1.,2.,3.,4.])

C = np.arange(2).reshape(-1,1) # column
R = np.arange(2).reshape(1,-1) # row

print( 'C = ', C )
print( 'R = ', R )
print( 'C + R = ', C + R ) # valid addition: array([[0.,1.],[1.,2.]])
'''
For instance, suppose a vector of size n is to be broadcast to the shape (m, n):
1. v is automatically reshaped to (1, n).
2. v is extended to (m, n).
'''
M = np.array([[11, 12, 13, 14], 
           [21, 22, 23, 24], 
           [31, 32, 33, 34]])
v = np.array([100, 200, 300, 400])
print( 'M + v = \n', M + v )

print( linecomment )
print( '''shape missmatch''')
print( linecomment )
M = np.array([[11, 12, 13, 14], 
           [21, 22, 23, 24], 
           [31, 32, 33, 34]])
v = np.array([100, 200, 300])
# M + v  # returns an error, v will automatically convert to (1,3)

print( 'M + v.reshape(-1,1) = ', M + v.reshape(-1,1) )

print( linecomment )
print( '''rescale rows and columns''')
print( linecomment )
coeff = np.array([1,10,100])
rescaled = M*coeff.reshape(-1,1) # rescale rows
print( 'rescaled = ', rescaled )

coeff = np.array([1,10,100,10000])
rescaled = M*coeff
print( 'rescaled = \n', rescaled )

rescaled = M*coeff.reshape(1,-1)
print( 'rescaled = \n', rescaled )

print( linecomment )
print('''functions of two variables''' )
print( linecomment )
u = np.arange(2)
v = np.arange(3)
W = u.reshape(-1,1)+v   # wij = ui + vj
print( 'W = ', W )

x = np.linspace(0,2*np.pi,5)
y = np.linspace(0,np.pi,3)
w = np.cos(x).reshape(-1,1)+np.sin(2*y)
print( 'w = ', w )

x,y = np.ogrid[0:1:3j,0:1:3j] # x,y are vectors with the contents of linspace(0,1,3)
w = np.cos(x) + np.sin(2*y)
print( 'w = ', w )  # 

print('--------------------------\n','ogrid')
x,y = np.ogrid[0:1:3j, 0:1:3j]
print('x = ', x )
print('y = ', y )

print('\n')
x,y = np.ogrid.__getitem__((slice(0, 1, 3j),slice(0, 1, 3j)))
print('x = ', x )
print('y = ', y )

x,y = np.ogrid[0:1.5:.5, 0:1.5:.5]
print('x = ', x)
print('y = ', y)