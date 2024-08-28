# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:31:51 2023

@author: lhoes
"""

import numpy as np
import matplotlib.pyplot as plt

h=0.001
y0=1

t=np.arange(0,10+h,h)
y=np.zeros(t.shape)
y[0]=1
exact=np.exp(-t)
error=np.zeros(t.shape)

for i in range(t.shape[0]-1):
   k1=-y[i]
   k2=-(y[i]+h/2*k1)
   k3=-(y[i]+h/2*k2)
   k4=-(y[i]+h*k3)
   y[i+1]=y[i]+h/6*(k1+2*k2+2*k3+k4)
   error[i]=(np.abs(exact[i]-y[i]))/y[i]

error[-1]=(np.abs(exact[-1]-y[-1]))/y[-1]
plt.plot(t,error)
#%%
plt.figure('Predict vs Exact')
plt.plot(t,y)
plt.plot(t,exact)  
plt.grid()  
#%%
plt.figure('Error compared to time')
plt.plot(t,error)
print(error.sum()/t.shape[0])
#the smaller h the better

#%%

h=0.01
y0=1

t=np.arange(0,10+h,h)
y=np.zeros(t.shape)
yp=np.zeros(t.shape)
y[0]=y0
yp[0]=-y0
exact=np.exp(-t)
error=np.zeros(t.shape)

for i in range(1,t.shape[0]):
    y[i]=y[i-1]+yp[i-1]*h
    yp[i]=-y[i]
    error[i]=(exact[i]-y[i])/y[i]
    
plt.figure('Error compared to time1')
plt.plot(t,error)
print(error.sum()/t.shape[0])
#the smaller h the better

h=0.1
y0=1

t=np.arange(0,10+h,h)
y=np.zeros(t.shape)
yp=np.zeros(t.shape)
y[0]=y0
yp[0]=-y0
exact=np.exp(-t)
error=np.zeros(t.shape)

for i in range(1,t.shape[0]):
    y[i]=y[i-1]+yp[i-1]*h
    yp[i]=-y[i]
    error[i]=(exact[i]-y[i])/y[i]
    
plt.figure('Error compared to time2')
plt.plot(t,error)
print(error.sum()/t.shape[0])
#the smaller h the better




