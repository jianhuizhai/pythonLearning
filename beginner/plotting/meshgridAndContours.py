#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

rosenbrockfunction = lambda x,y: (1-x)**2+100*(y-x**2)**2 
X,Y = np.meshgrid(np.linspace(-.5,2.,100), np.linspace(-1.5,4.,100))
Z = rosenbrockfunction(X,Y) 
plt.contour(X,Y,Z,np.logspace(-0.5,3.5,20,base=10),cmap='gray') 
plt.title('Rosenbrock Function: ')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

print('=*80')
print('Optimization and Rosenbrock\'s function')
import scipy.optimize as so
rosenbrockfunction = lambda x,y: (1-x)**2+100*(y-x**2)**2
X,Y= np.meshgrid(np.linspace(-.5,2.,100), np.linspace(-1.5,4.,100))
Z=rosenbrockfunction(X,Y)
cs=plt.contour(X, Y, Z, np.logspace(0,3.5,7,base=10),cmap='gray')
rosen=lambda x: rosenbrockfunction(x[0],x[1])
solution, iterates = so.fmin_powell(rosen,x0 = np.array([0,-0.7]),retall=True)
x,y=zip(*iterates)
plt.plot(x,y,'ko') # plot black bullets
plt.plot(x,y,'k:',linewidth=1) # plot black dotted lines
plt.title("Steps of Powell's method to compute a  minimum")
plt.clabel(cs)

plt.show()