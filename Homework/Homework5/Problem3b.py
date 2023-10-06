import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():

    x0 = np.array([1.0, 1.0, 1.0])
    
    Nmax = 100
    tol = 1e-10

    # After finding xstar numerically below, I created the point xstarfound below to compute error
    xstarfound = [1.09364232, 1.36032838, 1.36032838]
    
    t = time.time()
    for j in range(50):
      [xstar,ier,its] =  Newton(x0,tol,Nmax, xstarfound)
    elapsed = time.time()-t
    print(xstar)
    print('Newton: the error message reads:',ier)
    print('Newton: took this many seconds:',elapsed/50)
    print('Netwon: number of iterations is:',its)
       
def evalF(x): 

    F = np.zeros(3)
    
    F[0] = 2*x[0]
    F[1] = 8*x[1]
    F[2] = 8*x[2]
    return F

def evald(x): 
    
    d = ((x[0])**2 + 4*(x[1])**2 + 4*(x[2])**2 - 16)/((2*x[0])**2 + (8*x[1])**2 + (8*x[2])**2)
    return d


def Newton(x0,tol,Nmax, xstarfound):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    x1 = np.zeros(3)

    for its in range(Nmax):
       d = evald(x0)
       F = evalF(x0)

       error = (norm(x0 - xstarfound))
       print(error)
       x1 = x0 - d * F
       
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
