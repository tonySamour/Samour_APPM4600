# import libraries
import numpy as np
        
def driver():
#f = lambda x: (x-2)**3
#fp = lambda x: 3*(x-2)**2
#p0 = 1.2

  f = lambda x: np.exp(3*x)-27*(x**6)+27*(x**4)*np.exp(x) - 9*(x**2)*np.exp(2*x)
  fp = lambda x: 3*np.exp(3*x)- 6*27*x**5 + 27*((4*x**3)*(np.exp(x))+(x**4)*(np.exp(x)))-9*((2*x)*(np.exp(2*x))+ (2*x**2)*(np.exp(2*x)))
  fpp = lambda x: 9*np.exp(3*x)- 30*27*x**4 + 27*((12*x**2)*(np.exp(x))+(4*x**3)*(np.exp(x))+(4*x**3)*(np.exp(x))+(x**4)*(np.exp(x)))-9*((2)*(np.exp(2*x))+ (4*x)*(np.exp(2*x))+ (4*x)*(np.exp(2*x))+ (4*x**2)*(np.exp(2*x)))
  p0 = 4

  Nmax = 100
  tol = 1.e-14

  (p,pstar,info,it) = newton(f,fp,fpp,p0,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)


def newton(f,fp,fpp,p0,tol,Nmax):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """

  # Include multiplicity of root m = 2
  m = 2
  p = np.zeros(Nmax+1);
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-(f(p0)*fp(p0)/(fp(p0)**2-f(p0)*fpp(p0)))
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]
        
driver()