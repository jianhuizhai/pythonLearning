#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

# random vector with normal distribution
sigma, mu = 2, 10
x = sigma*np.random.standard_normal(10000)+mu 
plt.hist(x,50, density=True, color='b', facecolor='g')
z = np.linspace(0,20,200)
plt.plot(z, (1/np.sqrt(2*np.pi*sigma**2))*np.exp(-(z-mu)**2/(2*sigma**2)),'g')
# title with LaTeX formatting 
plt.title(r'Histogram with $\mu={},\ \sigma={}$'.format(mu,sigma))

plt.axis([0,20,0,0.25])

plt.show()