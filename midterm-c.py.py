# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:19:55 2019

@author: Ebrahim Amer
"""

import os, time
import numpy as np
import matplotlib.pyplot as plt

panel = 0
a = []
b = []
teta = [1]


            #KUTTA COND.
    
def Kutta_cond(a,b):
            w = []
            z = []
            for loop, item in enumerate(b):
                if(loop == int(1)):
                    break
                dyu = b[loop+1]-b[loop]
                dxu = a[loop+1]-a[loop]
                m1u = dyu/dxu
            n = a[::-1]
            m = b[::-1]
            for i in range(0, 2):
                w = np.append(w, n[i])
                z = np.append(z, m[i])
            for i, item in enumerate(w):
                if(i == int(1)):
                    break
                dyl = z[i]-z[i+1]
                dxl = w[i]-w[i+1]
                m1l = dyl/dxl
                if(abs(m1u) == abs(m1l)):
                    condition = print('IT IS POINTED')
                else:
                    condition = print('IT IS CUSPED')
                return condition
           
            plt.legend(loc='best')
            plt.plot(a,b, 'o')
            plt.axis('equal')
            plt.show()
            
            
            
            