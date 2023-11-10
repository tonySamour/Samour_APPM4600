import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def driver():

    f = lambda x: np.sin(x)
    # Taylor
    t = lambda x: x-(x**3)/6+(x**5)/120
   # pade rational approx
    #r = lambda x: (x - (7/60)*x**3)/(1 + (1/20)*x**2)
    r = lambda x: (360*x)/(360 + 60*(x**2) + 7*(x**4))

    a = 0
    b = 5
    
    Nint = 3
    # create chebychev nodes
    xint = np.zeros(Nint+1)
    for j in range(1,Nint+2):
       xint[j-1] = np.cos(np.pi*(2*j-1)/(2*(Nint+1)))
    # scale  for the interval
    m = (b-a)/2 
    c = (a+b)/2
    xint = m*xint+c
    xint = xint[::-1]
    
    yint = f(xint)


    # test the different evaluation methods
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
  
    # create the Lagrange evaluation
    yeval = np.zeros(Neval+1) 
    for kk in range(Neval+1):
       yeval[kk] = eval_lagrange(xeval[kk],xint,yint,Nint)       

    # compare the errors
    fex = f(xeval)
    f_rat = r(xeval)
    ft = t(xeval)

    plt.figure()

    plt.plot(xeval, fex, 'k-', label = 'f(x)')
    plt.plot(xeval, ft, 'g-', label = 'Taylor')
    plt.plot(xeval, f_rat, 'b-', label = 'Rational')
    plt.legend()
  
    plt.figure() 
    
    # plt.semilogy(xeval,abs(fex-yeval),'ro--',label='lagrange')
    plt.semilogy(xeval,abs(fex-ft),'g-',label='Taylor Error')
    plt.semilogy(xeval,abs(fex-f_rat),'b-',label='Rational Error')
    plt.legend()
    plt.show()
     




def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)
    
    
driver()    
       
