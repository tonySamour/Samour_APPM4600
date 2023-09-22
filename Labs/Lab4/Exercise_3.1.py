# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: 1+0.5*np.sin(x)
# fixed point is alpha1 = 1.4987....

     f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

     f3 = lambda x: (10/(x+4))**(1/2)
#fixed point is alpha2 = 1.365... 

     Nmax = 100
     tol = 10e-10
# f1 and f2 are test codes given in the example file. f1 is supposed to converge, f2 is not.
# f3 is given in the Pre-Lab, and used for 3.1

# test f1 
     x0 = 0.0
     [xstar,ier, iterations] = fixedpt(f1,x0,tol,Nmax)
     print('\nthe approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
     print('Iterations: \n', iterations)
    
#test f2 '''
     x0 = 0.0
     [xstar,ier, iterations] = fixedpt(f2,x0,tol,Nmax)
     print('\nthe approximate fixed point is:',xstar)
     print('f2(xstar):',f2(xstar))
     print('Error message reads:',ier)
     print('Iterations: \n', iterations)

#Lab 4 Pre-Lab 2.2.2 '''
     x0_3 = 1.5         # Given
     [xstar,ier, iterations] = fixedpt(f3,x0_3,tol,Nmax)
     print('\nthe approximate fixed point is:',xstar)
     print('f3(xstar):',f3(xstar))
     print('Error message reads:',ier)
     print('Iterations: \n', iterations)
     
# define routines

    # Lab 4 Exercise 3.1 Aitken's Method
def aitken (iterations, Nmax, xstar, tol):
     # Define empty vector take take in new iterated values
     iterations2=[]
     # Initialize counter
     count = 0
     # Loop to test the value of 'iterations' found using the fixed point method
     while (count < Nmax-2):
         # Aitken's method formula
         xn = iterations[count] - ((iterations[count+1]- xstar)**2)/(iterations[count+2]-2*iterations[count+1]+iterations[count])
         
         # Add new values of xn to empty vector
         iterations2.append(xn)

         # Add to counter
         count = count + 1

     # Check to see if xn is converging to xstar    
     if (abs(xn -xstar) < tol):
         # If converging, error message outputs 0
         ier2 = 0
         return[iterations2, ier2]
     # If xn does not converge to xstar, error message outputs 1
     ier2 = 1
     xstar = xn
     return [iterations2, ier2]

def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    iterations = np.zeros((Nmax,1))
    while (count <Nmax):
       iterations[count] = x0
       count = count +1
       x1 = f(x0)

       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier, iterations]
       x0 = x1

    xstar = x1
    ier = 1

     # Test code written in class for numerical way to find order of convergence
    """ e_top = abs(iterations[count + 1]-xstar)
    e_bottom = abs(iterations [count] - xstar)
    lambda_ = e_top/e_bottom
    print (lambda_)
    if lambda_ < 1:
        print ('The convergence is linear') """
    
    # Call subroutine aitken within fixedpt
    [iterations2, ier2] = aitken(iterations, Nmax, xstar, tol)
    print ('Aitken Method Iterations: ', iterations2)
    print ('Aitken Error message reads: ', ier2)
    
    return [xstar, ier, iterations]
    

driver()