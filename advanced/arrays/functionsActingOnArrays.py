#! /usr/bin/python3

import numpy as np

linecommnet = '='*80

print( linecommnet )
print('''Universal functions''')
print( linecommnet )

print( np.cos( np.pi) ) # -1
print( np.cos( np.array([[0, np.pi/2, np.pi]]) ) ) # array([[1, 0, -1]])

print( 2 * np.array([2, 4]) ) # array([4, 8])
print( np.array([1, 2]) * np.array([1, 8]) ) # array([1, 16])

print( np.array([1, 2])**2 ) # array([1, 4])
print( 2**np.array([1, 2]) ) # array([2, 4])
print( np.array([1, 2])**np.array([1, 2] ) ) # array([1, 4])

print( linecommnet )
print('''Create Universal Functions: vectorize''')
print( linecommnet )
def const(x):
    return 1
print( const(np.array([0, 2])) ) # returns 1 instead of array([1, 1])

def heaviside(x):
    if x >= 0:
        return 1.
    else:
        return 0.
'''
print( heaviside(np.array([-1, 2])) ) # error
'''
vheaviside = np.vectorize(heaviside)
print( vheaviside(np.array([-1,2])) ) # array([0,1]) as expected

import matplotlib.pylab as plt
xvals = np.linspace(-1,1,100)
plt.plot(xvals,np.vectorize(heaviside)(xvals))
plt.axis([-1.5,1.5,-0.5,1.5])
plt.show()

A = np.arange(1,9).reshape((2,-1))
print( 'A = ', A )

print( np.sum(A) ) # 36
print( np.sum(A, axis=0) ) # array([ 6,  8, 10, 12])
print( A.sum(axis=1) ) # array([10, 26])