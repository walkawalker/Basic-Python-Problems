# -*- coding: utf-8 -*-
import numpy as np 
import pandas as pd

#rank = int(input("Enter Integer Value for Rank: "))
defaultarray = [[21,31,23],[32,14,42],[3,5,7],[25,37,27],[29,17,42]]
defaultrank = 3
defaultarray2 = [[69, 420, 55], [66, 159, 342], [79, 335, 651], [445, 16, 79]]
defaultrank2 = 4

def findindex(testarray, rank):
    strarg = ''
    if rank == 2:
        strarg = str(rank) + 'nd'
    elif rank == 3:
        strarg = str(rank) + 'rd'
    else:
        strarg = str(rank) + 'st'
    sumarray = []
    keepidx = 0
    keepval = 0 
    for i in range(len(testarray)):
        sumarray.append([np.sum(testarray[i])])
    sumarray.sort(reverse = True)

    keepval = sumarray[rank-1]
    keepidx = rank
    for j in range(len(sumarray)):
        if sumarray[j] == keepval:
            if j < rank-1:
                keepval = sumarray[j]
                keepidx = j
    return print('The ', strarg, 'highest value is:\n', keepval, '\n', 'Its index in the array is:\n', keepidx) 

findindex(defaultarray, defaultrank)

findindex(defaultarray2, defaultrank2)



