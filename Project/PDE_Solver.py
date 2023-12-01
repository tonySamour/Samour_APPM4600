import matplotlib.pyplot as plt
import numpy as np
import math

from conj_grad_method import *

def driver():
    n = 10
    x0 = 0
    xf = 10

    tol = 1e-5

    A, b = FDM(x0, xf, n)

    y = CGM(A, b, n, tol)

    t = np.linspace(x0,xf,n+1)

    plt.figure()
    plt.plot(t, y)
    plt.plot


def FDM(x0, xf, n):
    
    h = (xf - x0)/n

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

    return A,b


driver()