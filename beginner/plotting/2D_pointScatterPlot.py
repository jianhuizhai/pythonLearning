#! /usr/bin/python3

import numpy as np
from matplotlib.pyplot import *

x1 = 2*np.random.standard_normal((2,100))
x2 = 0.8*np.random.standard_normal((2,100)) + np.array([[6],[2]])
plot(x1[0],x1[1],'*')
plot(x2[0],x2[1],'r*')
title('2D scatter plot')
show()