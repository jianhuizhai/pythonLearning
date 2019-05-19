#! /usr/bin/python3
from numpy import sin,cos

class Newton:
    tol = 1e-8 # this is a class attribute
    def __init__(self,f):
        self.f = f # this is not a class attribute
    ...

N1 = Newton(sin) 
N2 = Newton(cos)

print( N1.tol )
print( N2.tol )
Newton.tol = 1e-10
print( N1.tol )
print( N2.tol )
N2.tol = 1.e-4  # now N2.tol is detached from the class attribute
print( N1.tol )# still 1.e-10
print( N2.tol )

Newton.tol = 1e-5 # now all instances of the Newton classes have 1e-5
print( N1.tol ) # 1.e-5
print( N2.tol ) # 1e-4 but not N2.