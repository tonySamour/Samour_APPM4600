import matplotlib.pyplot as plt
import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm


def driver():

    #tolerance level
    tol = 1e-5

    # Matrix Size
    n = 3
    condition_number = 2

    
    # b vector, right hand side vector of system
    b = np.random.randn(n,1)

    A = spd_matrix(n, condition_number)
    print('SPD Matrix A is',A)
    print('The condition number of A is', np.linalg.cond(A))

    t = time.time()
    for j in range(50):
        [x,its] = CGM(A,b,n,tol)
    elapsed = time.time()-t
    print('CGM xstar is',x)
    print('real','CGM: took this many seconds:',elapsed/50)
    print('CGM iteration count is', its)

    t = time.time()
    for j in range(50):
        [x,its] = steepest(A,b,n,tol)
    elapsed = time.time()-t
    print('steepest xstar is',x)
    print('real','Steepest: took this many seconds:',elapsed/50)
    print('steepest iteration count is', its)
    

    

def spd_matrix(n, condition_number):  # inputs are size and condition number
    # generate a random matrix
    A = np.random.randn(n,n)


    # make it symmetric by adding its transpose
    A = np.dot(A,np.transpose(A))
   
    
    # AAt = QR
    Q = np.linalg.qr(A)[0]
  

    # Make eigenval matrix
    eigvals = np.linspace(1, 1/condition_number, n)
    eigvals_diag = np.diag(eigvals)


    # A = (Q * diag(eigvals) * Qt)
    A = np.matmul(Q, eigvals_diag)
    A = np.matmul(A,np.transpose(Q))

    

    return A


def steepest(A,b,n,tol):

    x = np.zeros(n)
    r = b - np.dot(A,x)
    
    its = 0
    
    while np.linalg.norm(r) >tol:
        v = r
        Av = np.dot(A,v)
        alpha = np.dot(v,r) / np.dot(v,Av)         
        x = x + (alpha*v)
        r  = r - (alpha*Av)

        its = its + 1

    return [x,its]   



def CGM(A,b,n,tol):

    x = np.zeros(n)
    r = b - np.dot(A,x)

    its = 0

    while np.linalg.norm(r) >tol:
        v = r
        Av = np.dot(A,v)
        alpha = np.dot(r,r) / np.dot(v,Av)         
        x = x + (alpha*v)
        r1  = r - (alpha*Av)
        beta = np.dot(r1,r1) / np.dot(r,r)
        v = r1 + (beta*v)
        r = r1

        its = its + 1
        
    return [x,its]

    
driver()    
       
