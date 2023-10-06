import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():

    x0 = np.array([1, 0])
    
    Nmax = 100
    tol = 1e-10
    h = 10e-7


    t = time.time()
    for j in range(50):
      [xstar,ier,its] =  Newton(x0,tol,Nmax, h)
    elapsed = time.time()-t
    print(xstar)
    print('Newton: the error message reads:',ier)
    print('Newton: took this many seconds:',elapsed/50)
    print('Netwon: number of iterations is:',its)
       
def evalF(x): 

    F = np.zeros(2)
    
    F[0] = 4*(x[0])**2 + (x[1])**2 - 4
    F[1] = x[0] + x[1] - np.sin(x[0]-x[1])
    
    return F
    ((x[0]) + (x[1]) - np.sin((x[0]) - (x[1])) - ((x[0]) + (x[1]) - np.sin((x[0]) - (x[1]))))/h
def evalJ(x,h): 

    J = np.array([[((4*(x[0] + h)**2 + (x[1])**2 - 4) - (4*(x[0])**2 + (x[1])**2 - 4))/h, ((4*(x[0])**2 + (x[1] + h)**2 - 4) - (4*(x[0])**2 + (x[1])**2 - 4))/h], 
                  [((x[0] + h) + (x[1]) - np.sin((x[0] + h) - (x[1])) - ((x[0]) + (x[1]) - np.sin((x[0]) - (x[1]))))/h, ((x[0]) + (x[1] + h) - np.sin((x[0]) - (x[1] + h)) - ((x[0]) + (x[1]) - np.sin((x[0]) - (x[1]))))/h]])
    return J


def Newton(x0,tol,Nmax, h):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
       J = evalJ(x0, h)
       Jinv = inv(J)
       F = evalF(x0)
       
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]
        
if __name__ == '__main__':
    # run the drivers only if this is called from the command line
    driver()       
