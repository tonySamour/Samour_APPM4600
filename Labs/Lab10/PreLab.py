import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 


def driver():
    
    n = 2
    x = np.linspace(0,10,11)
    

    p = eval_legendre(2,n)
    print(p)

def eval_legendre(x,n):
     phi = np.zeros(n+1)
     phi[0] = 1
     phi[1] = x
     for i in range(1,n):
          phi[i+1] = (1/(i+1))*((2*i+1)*x*(phi[i]) - i*(phi[i-1]))
     
     return phi          

if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()               
