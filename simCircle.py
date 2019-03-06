# -*- coding: utf-8 -*-
"""
Riddle simulation

Let r denote the radius of a circle. Let Q be a uniformly distributed point 
within this circle, and x be the distance from the centre of the circle and to
the point Q. What is E[x]?
"""

import random as rand
import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(shape=(1000000,1))
y = np.zeros(shape=(1000000,1))
ll=0
for ii in range(0,10000):
    xx = 10*rand.uniform(-1,1)
    yy = 10*rand.uniform(-1,1)
    d  = xx**2 + yy**2
    if d<=100:
        x[ll] = xx
        y[ll] = yy
        ll    = ll + 1
        
x = x[0:ll]
y = y[0:ll]        
    
fig = plt.figure()
ax = plt.axes()

ax.set_aspect(1)
theta = np.linspace(-np.pi, np.pi, 200)
plt.plot(np.sin(theta)*10, 10*np.cos(theta))
plt.scatter(x,y)
plt.show()


z = np.multiply(x,x)+np.multiply(y,y)
l = np.mean(np.sqrt(z))
print('\nE[x] = ' + str(l))
    