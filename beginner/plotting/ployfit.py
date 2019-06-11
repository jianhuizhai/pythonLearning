#! /usr/bin/python3

import numpy as np
from matplotlib.pyplot import *

# —Polyfit example—
x = range(5)
y = [1,2,1,3,5]
p2 = np.polyfit(x,y,2)
p4 = np.polyfit(x,y,4)

# plot the polynomials and points
xx = np.linspace(-1,5,200) 
plot(xx, np.polyval(p2, xx), label='fitting polynomial of degree 2')
plot(xx, np.polyval(p4, xx),
                label='interpolating polynomial of degree 4') 
plot(x,y,'*')

# set the axis and legend
axis([-1,5,0,6])
legend(loc='upper left', fontsize='small')
show()