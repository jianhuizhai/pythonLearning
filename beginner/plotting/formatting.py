#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

k = 0.2
x = [np.sin(2*n*k) for n in range(20)]
#plt.plot(x, color='green', linestyle='dashed', marker='o',markersize=12, linewidth=6) 
plt.plot(x, color='green', linestyle='dashed', marker='o', 
                       markerfacecolor='blue', markersize=12, linewidth=6)

plt.show()

plt.plot(x,'go')
plt.show()