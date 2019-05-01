# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:55:41 2019

@author: Ebrahim Amer
"""
import os, time
import numpy as np
import matplotlib.pyplot as plt



indexX =0 
indexY = 0

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


