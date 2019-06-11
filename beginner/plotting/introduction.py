#! /usr/bin/python3

import numpy as np
from matplotlib.pyplot import *

# plot sin(x) for some interval
x = np.linspace(-2*np.pi,2*np.pi,200)
plot(x, np.sin(x))

# plot marker for every 4th point
samples = x[::4]
plot(samples, np.sin(samples),'r*')

# add title and grid lines
title('Function sin(x) and some points plotted')
grid()

show()