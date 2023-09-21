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

# test f1 '''
     x0 = 0.0
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('\nthe approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
    
#test f2 '''
     x0 = 0.0
     [xstar,ier] = fixedpt(f2,x0,tol,Nmax)
     print('\nthe approximate fixed point is:',xstar)
     print('f2(xstar):',f2(xstar))
     print('Error message reads:',ier)

#Lab 4 Pre-Lab 2.2.2 '''
     x0_3 = 1.5         # Given
     [xstar,ier] = fixedpt(f3,x0_3,tol,Nmax)
     print('\nthe approximate fixed point is:',xstar)
     print('f3(xstar):',f3(xstar))
     print('Error message reads:',ier)

#Given f(x), find the first derivative f'(x) by hand
     f3_prime = lambda x: -(10**(1/2)/(2*(x+4)**(3/2)))
     lambda_ = abs(f3_prime(1.36523001))
     if lambda_ < 1:
         print(lambda_, 'The order of convergence is linear')
         return
     
# define routines

    # Lab 4 Exercise 3.1 Aitken's Method
def aitken (iterations, Nmax, xstar, tol):
     iterations2=[]
     count = 0
     while (count < Nmax):
         xn = iterations[count] - ((iterations[count+1]- xstar)**2)/(iterations[count+2]-2*iterations[count+1]+iterations[count])
         iterations2.append(xn)
     if (iterations2[xn+1]-iterations2[xn] < tol):
         ier2 = 0
         return[ier2]
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
          print(iterations)
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1

    """ e_top = abs(iterations[count + 1]-xstar)
    e_bottom = abs(iterations [count] - xstar)
    lambda_ = e_top/e_bottom
    print (lambda_)
    if lambda_ < 1:
        print ('The convergence is linear') """
    
    aitken(iterations, Nmax, xstar, tol)
    return [xstar, ier, iterations]
    


driver()