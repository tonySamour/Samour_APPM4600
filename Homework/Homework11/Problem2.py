import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from scipy.integrate import quad

def driver():

    # Function to integrate
    f = lambda x: x * np.cos(1/x)
    
    # Integration bounds
    a = 1e-10
    b = 1

    # N equispaced intervals
    # For Simpson's Rule, n =2k
    n = 6 

    x = np.linspace(a,b,n+1)
    
    I_CompSimp, simpEvalCount = compSimpson(a, b, x, f, n)

    Ieval = quad(f, a, b)

    errSimp = abs(Ieval - I_CompSimp)

    print('Composite Simpsons Approximation: ', I_CompSimp, 'Num Evaluations: ', simpEvalCount)
    print('Simpsons Error: ', errSimp)
    print('Built-In Quadrature: ', Ieval)

    
def compSimpson(a, b, x, f, n):
    h = (b-a)/n
    fSumEven = 0
    fSumOdd = 0 
    evalCount = 2
    
    for j in range(1, n-1):
        if (j%2) == 0:
            fSumEven = fSumEven + f(x[j])
            evalCount += 1
        
    for jj in range(1, n):
        if (jj%2) != 0:
            fSumOdd = fSumOdd + f(x[jj])    
            evalCount += 1

    I = (h/3)*(f(a) + 2*fSumEven + 4*fSumOdd + f(b))
    return I, evalCount
driver()