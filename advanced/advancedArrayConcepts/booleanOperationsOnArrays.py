#! /usr/bin/python3

import numpy as np

linecomment = '='*80

'''
You cannot use and , or , and not on Boolean arrays. Indeed, those operators force the
casting from array to Boolean, which is not permitted. Instead, we can use the operators
given in the following table (Table 5.1) for componentwise logical operations on Boolean
arrays:

Logic operator          Replacement for Boolean arrays
    A and B                     A & B
    A or B                      A | B
    not A                       ~ A
'''

A = np.array([True, True, False, False])
B = np.array([True, False, True, False])
### A and B # error!
print( 'A = ', A )
print( 'B = ', B )

print( 'A & B = ', A & B ) # array([True, False, False, False])

print( 'A | B = ', A | B ) # array([True, True, True, False])

print( ' ~ A = ', ~A ) # array([False, False, True, True])

data = np.linspace(1,100,100) # data
deviation = np.random.normal(size=100) # the deviations 
           #don't forget the parentheses in next statement!

# print( '(deviation<-0.5) = ',(deviation<-0.5) )
exceptional = data[ (deviation<-0.5) | (deviation>0.5) ] 
exceptional = data[ abs(deviation) > 0.5 ] # same result 
small = data[ (abs( deviation ) < 0.5) & ( data <5. ) ] # small deviation and data #don't forget the parentheses!
print( 'exceptional = ', exceptional )
print( 'small = ', small )