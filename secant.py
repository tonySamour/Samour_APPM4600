# import libraries
import numpy as np
        
def driver():
#f = lambda x: (x-2)**3
#fp = lambda x: 3*(x-2)**2
#p0 = 1.2

  f = lambda x: (x**6 - x - 1)
  p0 = 2
  p1 = 1

  Nmax = 100
  tol = 1.e-14

  (p,pstar,info,it) = secant(f,p0,p1,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)


def secant(f,p0,p1, tol,Nmax):
  """
  Newton iteration.
  
  Inputs:
    f    - function
    p0   - initial guess for left bound of root
    p1   - initial guess for right bound of root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1);
  p[0] = p0
  p[1] = p1

  if (abs(p0) == 0):
     pstar = p0
     ier =0
     return
  
  if (abs(p1) == 0):
     pstar = p1
     ier =0
     return
  
  q0 = f(p0)
  q1 = f(p1)

  for it in range(Nmax):
      if (abs(q1-q0) == 0):
         ier = 1
         pstar = p1
         return
      
      p2 = p1 - (q1*(p1-p0))/(q1-q0)
      p[it+1] = p2
      if (abs(p2-p1) < tol):
          pstar = p2
          info = 0
          return [p,pstar,info,it]
      p0 = p1; q0 = f(p1)
      p1 = p2; q1 = f(p2)

  pstar = p1
  info = 1
  return [p,pstar,info,it]
        
driver()