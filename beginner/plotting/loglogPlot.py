#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

# log both x and y axis 
x = np.linspace(0,10,200) 
plt.loglog(x,2*x**2, label = 'quadratic polynomial',
                            linestyle = '--', linewidth = 3)
plt.loglog(x,4*x**4, label = '4th degree polynomial',
                            linestyle = '-.', linewidth = 3)
plt.loglog(x,5*np.exp(x), label = 'exponential function', linewidth = 3)
plt.title('Logarithmic plots')
plt.legend(loc = 'best')
plt.axis([-0.01,10,10**-5,10**6])

plt.show()