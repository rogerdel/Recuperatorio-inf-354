# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:52:03 2020

@author: Roger
"""

from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np 
import os
import pandas as pd

letras = ["a","c","d","e","f", "g","h","i","j", "k"]
head = ["TYPE", "XX1","YY1",",XX2","YY2", "SIZE", "DIAG"]
dc = {
"a":1,"c":2,"d":3,"e":4,"f":5, "g":6,"h":7,"i":8,"j":9, "k":10
}
rdc = {
1:"a",2:"c",3:"d",4:"e",5:"f", 6:"g",7:"h",8:"i",9:"j",10:"k"
}
data = []
for dirname, _, filenames in os.walk('learn'):
    for filename in filenames:
        f = open("learn/"+filename)
        lines = f.read().splitlines()
        
        for i in lines:
            l = []
            ln = i.split(" ")
            for j in ln:
                if(j!= ""):
                    l.append(j)
            data.append(l)
print(data)
cont = {}
diag = {}
for i in data:
    if i[0] not in diag:
        diag[i[0]] = float(i[len(i)-1])
    else:
        diag[i[0]]+= float(i[len(i)-1])
        
    if i[0] not in cont:
        cont[i[0]] = 1
    else:
        cont[i[0]]+=1
        
for i in diag:
    diag[i] /= len(data)
    
for i in cont:
    print(f'total de {rdc[int(i)]} {cont[i]}')
print("-----------------------------")
for i in cont:
    print(f'promedio DIAG {rdc[int(i)]} {diag[i]}')