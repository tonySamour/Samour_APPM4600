import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from numpy.linalg import inv
def driver():


    f = lambda x: 1/(1+(10*x)**2)

    N = 20
    ''' interval'''
    a = -1
    b = 1
   
   
    ''' create equispaced interpolation nodes'''
    h = 2/(N-1)
    xint = np.array([(-1 + (i-1)*h) for i in range(1,N+2)])
    # xint = np.array([np.cos(((2*j-1)*np.pi)/(2*N)) for j in range(1,N+2)])

    ''' create interpolation data'''
    yint = f(xint)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)   
    
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
    y = np.zeros( (N+1, N+1) )

    ''' create vector with exact values'''
    fex = f(xeval)
       
    [ceval, poly_eval] = eval_polynomial(xint, xeval, yint, N)   
    plt.figure()    
    plt.plot(xeval,fex,'r', label = "Plotted function")
    plt.plot(xeval,poly_eval,'o', label = "Monomial Approximation") 
    plt.legend()

    plt.figure() 
    err_poly = abs(poly_eval-fex)
    plt.semilogy(xeval,err_poly,label='Monomial Error')
    plt.legend()
    plt.show()

def eval_polynomial(xint, xeval, yint, N):
   V = np.zeros([N+1,N+1])
   for r in range (N+1):
      for c in range (N+1):
         V[r][c] = xint[r]**c
   
   ceval = inv(V).dot(yint)
   poly = []

   for i in xeval:
        n = 0 
        for j in range(N+1):
            n += ceval[j] * i**j

        poly.append(n)

   return (ceval, poly)
         
driver()        
