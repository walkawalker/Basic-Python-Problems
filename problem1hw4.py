# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from scipy.ndimage import convolve

k1=2
rules1= ['dead', 'alive','dead', 'alive','dead', 'dead', 'dead', 'dead', 'dead', 'dead']
int_grid1 = [[1,0,1,0],[0,1,0,1]]

k2=2
rules2= ['dead', 'alive','alive', 'alive','dead', 'dead', 'dead', 'dead', 'dead', 'dead']
int_grid2 = [[1,0],[1,1],[0,1]]

k3 =4
rules3 = ['dead','alive','alive','dead','dead','dead','dead','dead','dead','dead','dead']
int_grid3 = [[1,1,1,0],[0,1,0,1],[0,0,1,0]]



def gridGame(grid, K, rules):
    newrules = []
    for l in rules:
        if l == 'dead':
            newrules.append(0)
        elif l == 'alive':
            newrules.append(1)
        else:
            print('Rerun the code and check you alive/dead rules')
    originalshape = np.shape(grid)
    gridt = np.array(grid)
    for j in range(0,K):
        transformgrid = []
        identitygrid = np.array([[1,1,1],[1,0,1],[1,1,1]])
        neighborsgrid = convolve(gridt, identitygrid, mode='constant')
        for i,row in enumerate(neighborsgrid):
            for index in neighborsgrid[i]:
                transformgrid.append(newrules[index])
        gridt = np.array(transformgrid).reshape(originalshape)
        del transformgrid
    return print(gridt)

gridGame(int_grid1, k1, rules1)
print('\n')
gridGame(int_grid2, k2, rules2)
print('\n')
gridGame(int_grid3, k3, rules3)