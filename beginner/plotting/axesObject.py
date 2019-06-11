#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(1)
ax = plt.subplot(111)
x = np.linspace(0,2*np.pi,100) 
# We set up a function that modulates the amplitude of the sin function
amod_sin = lambda x: (1.-0.1*np.sin(25*x))*np.sin(x)
# and plot both...
ax.plot(x, np.sin(x),label = 'sin') 
ax.plot(x, amod_sin(x), label = 'modsin')

plt.show()