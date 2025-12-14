#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 20:17:26 2025

@author: dustindocusen
"""

import matplotlib.pyplot as plt
import numpy as np

g = 9.81 #m/s^2
dt = 0.1 #s
p = 400 #W
m = 70 #kg
C = 0.9 
A = 0.33 #m^2
rho = 1.225 #kg/m^3
eta = 2e-5 #Pa * s
h = 2 #m
V = [4] #m/s
T = [0] #s
endtime = 50 #s
trange = int(endtime/dt)
grade = 0.1
theta = np.arctan(grade)

#Define dv/dt
def myODE(v):
    return (p/(m*v))-((0.5*C*rho*A*v**2)/m)-(eta*A*(v/h)/m)-g*np.sin(theta)

#Second order Runge-kutta estimation
def rk2step(vn):
    k1 = dt * myODE(vn)
    k2 = dt * myODE(vn + k1/2)
    return vn + k2

#Iterate over time range
for j in range(trange):
    V.append(rk2step(V[-1]))
    T.append(dt*(j+1))
    
#Plot results
plt.plot(T,V)
plt.title('Velocity vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
#plt.savefig('bicycleEC.png')
