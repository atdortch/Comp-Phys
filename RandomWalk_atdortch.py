# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:10:05 2018

@author: Aus
"""

import numpy as np
import random as rand
import matplotlib.pyplot as plt



particles = 100
steps = np.arange(1000)
Nsteps = 1000



position = np.zeros(Nsteps)      # position of particles start at zero

right = 1; left = 2                 # assign values to left and right positions

for step in steps:           
    for p in range(particles):
        walk = rand.randint(1,2)
        if walk == right:
            position[step] += 1
        elif walk == left:
            position[step] -=1
displacement = position-0

print(position)

plt.plot(steps,displacement,'og')



#----------------------------------------------------------------------

import numpy as np
import random as rand
import matplotlib.pyplot as plt



particles = 100
steps = np.arange(1000)
Nsteps = 1000



position = np.zeros(Nsteps)      # position of particles start at zero

right = 1; left = 2                 # assign values to left and right positions

for step in steps:           
    for p in range(particles):
        walk = rand.randint(1,2)
        if walk == right:
            position[step] += 1
        elif walk == left:
            position[step] -=3
displacement = position-0

print(position)

plt.plot(steps,displacement,'og')


#-------------------------------------------------------------------------

import numpy as np
import random as rand
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

x = []
y = []
z = []

particles = 100
steps = np.arange(1000)
Nsteps = 1000



position = np.zeros(Nsteps)      # position of particles start at zero

right = 1; left = 2; forward = 3; backward = 4; up = 5; down = 6

x3d = 0
y3d = 0
z3d = 0


for step in steps:           
    for p in range(particles):
        walk3D = rand.randint(1,7)
        
        if walk == right:
            x3d = 1
            x.append(x3d)
        elif walk == left:
            x3d = -1
            x.append(x3d)
        elif walk == forward:
            y3d = 1
            y.append(y3d)
        elif walk == backward:
            y3d = -1
            y.append(y3d)
        elif walk == up:
            z3d = 1
            z.append(z3d)
        elif walk == down:
            z3d = -1
            z.append(z3d)

print(position)
Axes3D.plot(x,y,z)
plt.show()





