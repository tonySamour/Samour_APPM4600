import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

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
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_bary= np.zeros(Neval+1)
  
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
    y = np.zeros( (N+1, N+1) )
     
    
    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_bary[kk] = eval_barycentric(xeval[kk],xint,yint,N)

    ''' create vector with exact values'''
    fex = f(xeval)
       

    plt.figure()    
    plt.plot(xeval,fex,'r')
    plt.plot(xeval,yeval_bary,'o', label = 'Barycentric Approximation') 
    plt.legend()

    plt.figure() 
    err_bary = abs(yeval_bary-fex)
    plt.semilogy(xeval,err_bary,'ro--',label='Barycentric Error')
    plt.legend()
    plt.show()

def eval_barycentric(xeval,xint,yint,N):

    wj = np.ones(N+1)

    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              wj[count] = 1/(wj[count]*(xint[jj] - xint[count]))

    numerator = 0
    denominator = 0
    
    for i in range(N+1):
        if (xeval != xint[i]):
           numerator += ((wj[i]*yint[i])/(xeval - xint[i]))
           denominator += (wj[i]/(xeval - xint[i]))
    
    yeval = numerator / denominator
  
    return yeval

driver()        
