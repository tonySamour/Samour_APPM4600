# import libraries
import numpy as np

def driver():

# use routines    
    f = lambda x: x**2 * (x - 1)
    
# Interval for (a)
    a1 = 0.5
    b1 = 2

# Interval for (b)
    a2 = -1
    b2 = 0.5

# Interval for (c)
    a3 = -1
    b3 = 2

    # tolerance for how close we should get to the root
    tol = 1e-7

    # Problem 1 (a)
    [astar1,ier1] = bisection(f,a1,b1,tol)
    print('\nProblem 1 (a)')
    print(' the approximate root is',astar1)
    print(' the error message reads:',ier1)
    print(' f(astar) =', f(astar1))

    # Problem 1 (b)
    [astar2,ier2] = bisection(f,a2,b2,tol)
    print('\nProblem 1 (b)')
    print(' the approximate root is',astar2)
    print(' the error message reads:',ier2)
    print(' f(astar) =', f(astar2))

    # Problem 1 (c)
    [astar3,ier3] = bisection(f,a3,b3,tol)
    print('\nProblem 1 (c)')
    print(' the approximate root is',astar3)
    print(' the error message reads:',ier3)
    print(' f(astar) =', f(astar3), '\n')




# define routines
def bisection(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier]
      
driver()               