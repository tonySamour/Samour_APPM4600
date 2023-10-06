import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():

    x0 = np.array([1.0, 0.0])
    
    Nmax = 100
    tol = 1e-10
    tol2 = 1e-4

    t = time.time()
    for j in range(50):
      [xstar,ier,its, NumJ] =  SlackerNewton(x0,tol,tol2,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Slacker Newton: the error message reads:',ier)
    print('Slacker Newton: took this many seconds:',elapsed/50)
    print('Slacker Netwon: number of iterations is:',its)
    print('Slacker Newton: Number of Jacobians taken:', NumJ)

def evalF(x): 

    F = np.zeros(2)
    
    F[0] = 4*(x[0])**2 + (x[1])**2 - 4
    F[1] = x[0] + x[1] - np.sin(x[0]-x[1])
    
    return F

def evalJ(x): 
    
    J = np.array([[8*x[0], 2*x[1]], 
                  [1 - np.cos(x[0]-x[1]), 1 + np.cos(x[0]-x[1])]])
    return J

def SlackerNewton(x0,tol,tol2,Nmax):
    
    ''' The goal of Slacker Newton Method is to take Jacobians until the differnce between iterates satisfies a
        certain tolerance. Once this tolerance is satisfied, the program uses Lazy Newton'''
    
    ''' inputs: x0 = initial guess, tol = tolerance to stop iterating, tol2 = tolerance to keep taking Jacobians, 
        Nmax = max iterations'''
    
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = evalJ(x0)
    Jinv = inv(J)
    # Number of Jacobians taken
    NumJ = 1
    
    for its in range(Nmax):
       
       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)
       
       # Check if the distance between x1 and x0 is larger than the tolerance set
       # This will continue to evaluate with every iteration until the condition is satisfied
       if (norm(x1-x0) > tol2):
         J = evalJ(x0)
         Jinv = inv(J)
         NumJ +=1

       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its, NumJ]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its, NumJ]
                
        
if __name__ == '__main__':
    # run the drivers only if this is called from the command line
    driver()       
