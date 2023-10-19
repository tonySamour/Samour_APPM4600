import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv

def driver():
    xeval = np.linspace(0,10,1000)
    xint = np.linspace(0,10,11)

    intervals = findx(xeval, xint)
    

def findx(xeval, xint):
    temp = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(1, len(xint)):
        temp2 = np.where((xeval<xint[i]) & (xeval >= xint[i-1]))
        temp[i-1] = xeval[temp2]
    temp[9] = np.append(temp[9],xeval[-1])
    return temp
    

def createLine(f, intervals):
   feval = f(intervals)
   slope = np.zeros(len(intervals), len(intervals[0]))
   for i in range(0,len(intervals)):
        for j in range(1, len(intervals)):
            slope[i][j-1] = (feval[i][j-1] - feval[i][j])/(intervals[i][j-1] - intervals[i][j])
        slope[i][-1] = (feval[i][-1] - feval[i][-2])/(intervals[i][-1] - intervals[i][-2])
    
    y - feval = slope*(x-intervals)
   
   return slope


driver()