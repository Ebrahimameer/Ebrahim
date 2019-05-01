# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 21:07:51 2019

@author: Ebrahim Amer
"""
import os, time
import numpy as np
import matplotlib.pyplot as plt


teta = [1]
indexX =0 
indexY = 0
x_n = []
y_n = []     
                   #MEAN CAMBER AND CHORD LINE CODE 
for root, dir, files in os.walk("Normalized Airfoil Dataset") :
    for i,j in enumerate (files):
        
        foilname = 'Normalized Airfoil Dataset/'+j
        
        fol = get_foil_coordinates(foilname)
        
        foilx, foily = fol[:,0], fol[:,1]
        
        print (i,j, len(foilx), len(foily)) 
       
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
            
            plt.plot(line_x, line_y, label='Maximum Thickness')
            plt.plot(xMCamber, plotMCamber, label='Mean Chamber Line')
            plt.plot(foilx,foily,label='Upper and Lower Surface')
            plt.plot(cor1,cor2, 'o-')
         