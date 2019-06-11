#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d

# example
fig = plt.figure()
ax = fig.gca(projection='3d')
# plot points in 3D
class1 = 0.6 * np.random.standard_normal((200,3))
ax.plot(class1[:,0],class1[:,1],class1[:,2],'o')
class2 = 1.2 * np.random.standard_normal((200,3)) + np.array([5,4,0])
ax.plot(class2[:,0],class2[:,1],class2[:,2],'o')
class3 = 0.3 * np.random.standard_normal((200,3)) + np.array([0,3,2])
ax.plot(class3[:,0],class3[:,1],class3[:,2],'o')

plt.show()

#========================================================================================
# surface plot
#========================================================================================
X,Y,Z = axes3d.get_test_data(0.05)

fig = plt.figure()
ax = fig.gca(projection='3d')
# surface plot with transparency 0.5 
ax.plot_surface(X,Y,Z,alpha=1.0)

plt.show()

# contour plots

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(X,Y,Z,rstride=5,cstride=5)

# plot contour projection on each axis plane
ax.contour(X,Y,Z,zdir='z',offset=-100)

ax.contour(X,Y,Z,zdir='x',offset=-40)
ax.contour(X,Y,Z,zdir='y',offset=40)

# set axis limits
ax.set_xlim3d(-40,40)
ax.set_ylim3d(-40,40)
ax.set_zlim3d(-100,100)

# set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()