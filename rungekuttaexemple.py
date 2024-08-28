# -*- coding: utf-8 -*-
"""
Created on Thu May  4 10:12:09 2023

@author: lhoes
"""

import numpy as np
h=1 #day
G=(2.95824*10**-4)
A=2
mo=1

t=np.arange(0,10000+h,h)
u=np.zeros((t.shape[0],6))
u[0]=np.array([A, 0, 0, 0, (G/A)**(1/2),0])

def f(u,t):
    return np.array([u[3], u[4], u[5], -G*mo/((u[0]**2+u[1]**2+u[2]**2)**(3/2))*u[0], -G*mo/((u[0]**2+u[1]**2+u[2]**2)**(3/2))*u[1], -G*mo/((u[0]**2+u[1]**2+u[2]**2)**(3/2))*u[2]])


for i in range(t.shape[0]-1):
   k1=f(u[i],t[i])
   k2=f(u[i]+h/2*k1,t[i]+h/2)
   k3=f(u[i]+h/2*k2,t[i]+h/2)
   k4=f(u[i]+h*k3,t[i]+h)
   u[i+1]=u[i]+h/6*(k1+2*k2+2*k3+k4)
   