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
    

def createLine(x, yeval, f):
   y = np.zeros((len(x), len(x[0])))
   for i in range(0,len(x)):
        for j in range(1, len(x)):
             slope = (yeval[i][j] - yeval[i][j-1])/(x[i][j] - x[i][j-1])
             y[i][j] = slope*(x[i][j] - x[i][j-1]) + yeval[i][j-1]
        return y
   return y

driver()