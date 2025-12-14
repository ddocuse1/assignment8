#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 11:09:12 2025

@author: dustindocusen
"""

#Random walk

import numpy as np
from matplotlib import pyplot as plt
import random

nsteps = 100
nwalkers = 500
displacement2D = []
meanDisplacement = []
meanDisplacement2 = []

for walker in range(nwalkers):
    x = [0]
    steps = [0]
    for step in range(nsteps):
        x.append(x[-1]+random.choice([-1,1]))
        steps.append(step+1)
    displacement2D.append(x)
    #plt.plot(steps,x)

for i in range(len(displacement2D[0])):
    totalDisplacement = 0
    totalDisplacement2 = 0
    for j in range(len(displacement2D)):
        totalDisplacement += displacement2D[j][i]
        totalDisplacement2 += displacement2D[j][i]**2
    meanDisplacement.append(totalDisplacement/len(displacement2D))
    meanDisplacement2.append(totalDisplacement2/len(displacement2D))

plt.plot(steps, meanDisplacement, label='<$x_n$>')
plt.plot(steps, meanDisplacement2, label='<$x_n^2$>')

plt.title('Mean Displacement Squared vs Step Number')
plt.xlabel('Step number')
plt.ylabel('Mean Displacement Squared')
plt.legend()
#plt.savefig('rwalkMeans.png')