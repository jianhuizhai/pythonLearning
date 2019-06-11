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

for il,line in enumerate(ax.lines):
    if line.get_label() == 'sin':
       break

# modifying line properties
print( ax.lines[il].properties().keys() )

ax.lines[il].set_linestyle('-.')
ax.lines[il].set_linewidth(2)

# modifying data
ydata=ax.lines[il].get_ydata()
ydata[-1]=-0.5
ax.lines[il].set_ydata(ydata) 

# annotations
annot1=ax.annotate('amplitude modulated\n curve', (2.1,1.0),(3.2,0.5),
       arrowprops={'width':2,'color':'k', 'connectionstyle':'arc3,rad=+0.5', 
                   'shrink':0.05},
       verticalalignment='bottom', horizontalalignment='left',fontsize=15, 
                   bbox={'facecolor':'gray', 'alpha':0.1, 'pad':10})
annot2=ax.annotate('corrupted data', (6.3,-0.5),(6.1,-1.1),
       arrowprops={'width':0.5,'color':'k','shrink':0.1},
       horizontalalignment='center', fontsize=12)
# remove the annotation
annot1.remove()

# filling areas between curves
axf = ax.fill_between(x, np.sin(x), amod_sin(x),facecolor='gray')
axf.remove()
axf = ax.fill_between(x, np.sin(x), amod_sin(x),where=amod_sin(x)-np.sin(x) > 0, facecolor='gray')

# ticks and ticklabels
ax.set_xticks(np.array([0,np.pi/2,np.pi,3/2*np.pi,2*np.pi]))
ax.set_xticklabels((r'$0$',r'$\mathcal{\pi/2}$',r'$\mathsf{\pi}$',r'$\mathtt{3/2 \pi}$',r'$2 \pi$'),fontsize=18)
ax.set_yticks(np.array([-1.,0.,1]))
ax.set_yticklabels(('$-1$','$0$','$1$'),fontsize=18)

fig.savefig('amp_mod_sin2a.png',dpi=300,transparent=True,bbox_inches='tight')

plt.show()