# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:48:30 2019

@author: Ebrahim Amer
"""

# Midterm_project
import os, time
import numpy as np
import matplotlib.pyplot as plt




panel = 0
a = []
b = []
teta = [1]
indexX =0 
indexY = 0
x_n = []
y_n = []


def get_foil_coordinates (foilname):
        
    with open (foilname) as f:
        content = f.readlines()
     
    arry = []
        
    for i in content:
        elements = i.strip().split()
        if len(elements) == 2:
            try:
                x,y = float(elements[0]),float(elements[1])
#                print(x,y)
                arry.append([x,y])
            except :
                pass
#                print ('not numbers')
                
    arry = np.array(arry)
    
    return arry



for root, dir, files in os.walk("Normalized Airfoil Dataset") :
    for i,j in enumerate (files):
        
        foilname = 'Normalized Airfoil Dataset/'+j
        
        fol = get_foil_coordinates(foilname)
        
        foilx, foily = fol[:,0], fol[:,1]
        
        print (i,j, len(foilx), len(foily))
        
       
            
        #MEAN CAMBER AND CHORD LINE CODE 
        
        plotMCamber = []
        xMCamber = []
        cor1=[min(foilx),foilx[len(foilx)-1]]
        cor2=[foily[int(len(fol)/2)],foily[len(foily)-1]]
            
        for loop, item in enumerate(foilx):
            if(loop == int(foilx.size/2)):
                break
            xMCamber = np.append(xMCamber,(item))
    
        for loop, item in enumerate(foily):
            
            if(loop == int(foily.size/2)):
                break
            
            plotMCamber = np.append(plotMCamber,(foily[loop]+foily[(foily.size-1-loop)])/2)
        
        #MAXIMUM THICKNESS AND POSITION CODE
        for loop, item in enumerate(foily):
            line_y = [np.max(foily), np.min(foily)]
            line_x = [foilx[foily.argmax()], foilx[foily.argmax()]]
            #################################################################

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

        plt.figure(figsize=(8,5))
        plt.xlabel('X Coordinates', fontsize=14)
        plt.ylabel('Y Coordinates', fontsize=14)
        plt.grid()
        plt.title(foilname)
        plt.plot(line_x, line_y, label='Maximum Thickness')
        plt.plot(xMCamber, plotMCamber, label='Mean Chamber Line')
        plt.plot(foilx,foily,label='Upper and Lower Surface')
        plt.plot(cor1,cor2, 'o-')
        plt.legend(loc='best')
#        plt.plot(a,b, 'o')
        plt.axis('equal')
        plt.show()