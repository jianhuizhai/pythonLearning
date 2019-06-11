#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import visvis.vvmovie as vv

# create initial function values
x = np.linspace(-255,255,511)
X,Y = np.meshgrid(x,x)
f = np.sqrt(X*X+Y*Y) - 40 #radius 40

# evolve and store in a list
imlist = []
for iteration in range(200):
    #print( 'iteration = ', iteration)
    #print((f>0))
    imlist.append((f>0)*255)
    f -= 1 # move outwards one pixel
vv.images2swf.writeSwf('circle_evolution.swf',imlist)

'''
# create initial function values
x = np.linspace(-255,255,511)
X,Y = np.meshgrid(x,x)
f = np.sqrt(X*X+Y*Y) - 40 #radius 40
for iteration in range(200):
	plt.imshow((f>0)*255)
	plt.gray()
	plt.axis('off')
	plt.savefig('circle_evolution_{:d}.png'.format(iteration))
	f -= 1
'''