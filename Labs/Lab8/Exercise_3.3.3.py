import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 


def driver():
    
    f = lambda x: math.exp(x)
    a = 0
    b = 1
    
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(a,b,Neval)
    
    ''' number of intervals'''
    Nint = 10
    
    '''evaluate the linear spline'''
    yeval = eval_cubic_spline(xeval,Neval,a,b,f,Nint)
    
    ''' evaluate f at the evaluation points'''
    fex = np.zeros(Neval)
    for j in range(Neval):
      fex[j] = f(xeval[j]) 
      
    
    plt.figure()
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yeval,'bs-')
    plt.legend()
    plt.show 
     
    err = abs(yeval-fex)
    plt.figure()
    plt.plot(xeval,err,'ro-')
    plt.show 
    
def findx(xeval, xint):
    temp = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(1, len(xint)):
        temp2 = np.where((xeval<xint[i]) & (xeval >= xint[i-1]))
        temp[i-1] = xeval[temp2]
    temp[9] = np.append(temp[9],xeval[-1])
    return temp
    
def createM(Neval):
    M = np.zeros((Neval-1,Neval-1))
    for r in range (0,Neval-1):
       for c in range(0, Neval-1):
          if r == c:
             M[r][c] = 1/3
          elif (r == c + 1) or (r == c - 1):
             M[r][c] = 1/12
          else:
             M[r][c] = 0

    return M

def evalMsystem(M,xint,f, Neval):
   h = xint[1] - xint[0]
   yint = np.zeros(len(xint))
   for j in range(0, len(xint)):
      yint[j] = f(xint[j]) 

   F = np.zeros(Neval-1)
   for i in range(1,Neval-1):
      F[i] = (yint[i+1] - 2*yint[i] + yint[i-1])/2*(h**2)
   Meval = inv(M)*F
   return Meval

def evalCubicPolynommial(Mi, Mi1, xi, xi1, fxi, fxi1):
   hi = xi1 - xi
   C = fxi/hi - (Mi*hi)/6
   D = fxi1/hi - (Mi1*hi)/6
   Si = lambda x: (Mi*(xi1 - x)**3)/(6*hi) + (Mi1*(x - xi)**3)/(6*hi) + C*(xi1 - x) + D*(x - xi)
   return Si
    
def  eval_cubic_spline(xeval,Neval,a,b,f,Nint):

    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)
   
    '''create vector to store the evaluation of the linear splines'''
    yeval = np.zeros(Neval) 
    
    M = createM(Nint)
    
    for jint in range(Nint):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        '''let n denote the length of ind'''
        ind = findx(xeval, xint)
        n = len(ind)
        
        '''temporarily store your info for creating a line in the interval of 
         interest'''
        a1= xint[jint]
        fa1 = f(a1)
        b1 = xint[jint+1]
        fb1 = f(b1)
        Meval = evalMsystem(M, xint,f, Nint)
        
        for kk in range(n):
           '''use your line evaluator to evaluate the lines at each of the points 
           in the interval'''
           '''yeval(ind(kk)) = call your line evaluator at xeval(ind(kk)) with 
           the points (a1,fa1) and (b1,fb1)'''
           yeval[ind[jint][kk]] = evalCubicPolynommial(Meval[jint][kk], Meval[jint][kk+1], a, b, fa1, fb1)
           
           
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()     

# I do not know how to get the functions to run. Not sure why my indices are messed up.
# If I get it to run I will reupload so I can use the code for the next HW.
# I'll try to go to Office hours next week. Once the code is running,
# it will be easy to plug in for different functions.
