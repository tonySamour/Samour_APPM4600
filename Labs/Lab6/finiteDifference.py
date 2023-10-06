# import libraries
import numpy as np

def driver():

    f = lambda x: np.cos(x)
    h = 0.01*2**(-np.arange(0,10))
    x0 = 0.0

    [ier, fp1] = forwardDifference(f, x0, h)

def forwardDifference(f, x0, h):
    
    
