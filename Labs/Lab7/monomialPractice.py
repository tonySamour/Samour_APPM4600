import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from numpy.linalg import inv 

def driver():


    f = lambda x: 1/(1+(10*x)**2)

    N = 3
    ''' interval'''
    a = -1
    b = 1
   
    ''' Interpolation nodes '''
    h = 2/(N-1)
    j = np.linspace(0,N, N+1)

    ''' create equispaced interpolation nodes'''
    xint = -1 + (j-1)*h
    
    ''' create interpolation data'''
    yint = f(xint)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_l= np.zeros(Neval+1)
    yeval_dd = np.zeros(Neval+1)
  
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
 
    


    ''' create vector with exact values'''
    fex = f(xeval)

    V = evalMonomial(xeval, fex, N)
    print(V)


def evalMonomial(xeval, fex, N):
   count = 0
   V = np.empty(shape = (N,N))
   while (count < N+1):
      xelement = (xeval[count])**count
      V = np.append(V[0], xelement, axis =1)
      count = count + 1
      return V
   Vinv = inv(V)
   aeval = Vinv*fex
   return V, aeval

driver()        
