#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def avg(x):
    """ simple running average """
    return (np.roll(x,1) + x + np.roll(x,-1)) / 3
# sine function with noise
x = np.linspace(-2*np.pi, 2*np.pi,200)
y = np.sin(x) + 0.4*np.random.rand(200)

# make successive subplots
for iteration in range(3):
    plt.subplot(3, 1, iteration + 1)
    plt.plot(x,y, label = '{:d} average{}'.format(iteration, 's' if iteration > 1 else ''))
    plt.yticks([])
    plt.legend(loc = 'lower left', frameon = False)
    y = avg(y) #apply running average 
plt.subplots_adjust(hspace = 0.7)
plt.savefig('test.pdf')  # save to pdf
plt.savefig('test.svg')  # save to svg (editable format)
plt.savefig('test1.pdf', transparent=True) 
plt.savefig('test2.pdf', bbox_inches='tight')
#plt.show()