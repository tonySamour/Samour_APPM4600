import matplotlib.pyplot as plt
import numpy as np
import math

def driver():
    
    n = 10
    a = 0
    b = 10
    h = (b - a)/n


    # Create matrix for derivatives

    A = np.zeros((n+1, n+1))
    A[0,0] = 1
    A[n,n] = 1
    for i in range (1, n):
        A[i, i-1] = 1
        A[i, i] = -2
        A[i, i+1] = 1
    
    # Get b vector
    b = np.zeros(n+1)
    b[0] = 0
    b[1:-1] = -9.8*h**2
    b[-1] = 50

driver()