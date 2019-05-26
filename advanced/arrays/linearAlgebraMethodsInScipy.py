#! /usr/bin/python3

import numpy as np
import scipy.linalg as sl

A = np.array([[1,2], [-6,4]])
[LU,piv] = sl.lu_factor(A)
print( 'LU = ', LU )
print( 'piv= ', piv)

bi = np.array([1,1])
xi=sl.lu_solve((LU,piv),bi)
print( xi )