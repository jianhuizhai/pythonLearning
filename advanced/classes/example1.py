#! /usr/bin/python3

linecomment = '==================================================================='

import numpy as np

class rationalNumber:
    
    def __init__(self, numerator, denominator):  # initialize class with initial values
        self.numerator = numerator
        self.denominator = denominator
    
    def convert2float(self):
        return float(self.numerator)/float(self.denominator)
    def __repr__(self):
        return '{} / {}'.format(self.numerator,self.denominator)

    def __add__(self, other):
        p1, q1 = self.numerator, self.denominator
        if isinstance(other, int):
            p2, q2 = other, 1
        else:
            p2, q2 = other.numerator, other.denominator
        return rationalNumber(p1 * q2 + p2 * q1, q1 * q2)
    def __eq__(self, other):
        return self.denominator * other.numerator == \
               self.numerator * other.denominator
    def __radd__(self, other):
        return self + other

q = rationalNumber(10, 20)
print(q.numerator)
print(q.denominator)
print(q.convert2float())  # this is equal to rationalNumber.convert2float(q)
print( q )  # __repr__ method
q = rationalNumber(1, 2)
p = rationalNumber(1, 3)
#print( q.add(p) )  # returns the RationalNumber for 5/6, this can be used when __add__ is changed to add
print( q + p)
print( q.__add__(p) )
p = rationalNumber(1, 2) # instantiation
q = rationalNumber(2, 4) # instantiation
print( p == q  )# True

p = rationalNumber(1, 2) # instantiation
print( p + 5 ) # corresponds to p.__add__(5) 
print( 5 + p ) # reverse add method

print( linecomment )
a = np.array([1,2])
print( a.shape )

print(linecomment)
z = 5 + 4j
print( z.imag )