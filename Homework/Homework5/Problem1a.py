# import libraries
import numpy as np
from numpy import linalg as LA
    
def driver():

# test functions 
    f = lambda x,y: 3*(x**2) - y**2
    g = lambda x,y: 3*x*y**2 - x**3 - 1

    J = [[1/6, 1/18],
         [0,   1/6]]

    Nmax = 100
    tol = 1e-6

# test f1 '''
    x0 = 1.0
    y0 = 1.0
    [xstar,ier] = fixedpt(f,g,x0,y0,J,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f(xstar):',f(xstar))
    print('Error message reads:',ier)


# define routines
def fixedpt(f,g,x0,y0,J,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    Xn = [[x0], 
          [y0]]
    F  = [[f(x0, y0)],
          [g(x0, y0)]]

    count = 0

    if (LA.norm(Xn - F[0][1])==0):
        xstar = Xn
        ier = 0
        return
    
    while (count <Nmax):
       count = count +1
       x1 = Xn - J* [[f(Xn[0][0],Xn[1][0])],
                     [g(Xn[0][0],Xn[1][0])]]
       
       if (LA.norm(x1 - Xn) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       Xn = x1

    xstar = x1
    ier = 1
    return [xstar, ier]
    

driver()