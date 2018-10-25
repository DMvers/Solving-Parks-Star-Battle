#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 17:06:15 2018

@author: david
"""
import skimage
import skimage.io
import os
import tkinter as tk
from tkinter import filedialog
import numpy as np

#Load screenshots and derive the problem from them
def loaddata():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory() 
    probs = []
    for filename in os.listdir(folder):
        test = folder + "/" + filename
        img = skimage.io.imread(test)
        probgrid = []
        for y in range(6):
            for x in range(6):
                thisx = x*183 + 60
                thisy = y*183 + 600
                probgrid.append(img[thisy][thisx][0])
        for i in range(len(probgrid)):
            
            #Assign each color to a different group
            if probgrid[i] == 127:
                probgrid[i] = 2
            if probgrid[i] == 128:
                probgrid[i] = 3
            if probgrid[i] == 138:
                probgrid[i] = 4
            if probgrid[i] == 234:
                probgrid[i] = 5
        probs.append(np.array(probgrid))
    return(probs)