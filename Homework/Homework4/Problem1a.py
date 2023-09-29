# import libraries
import numpy as np
import scipy
import matplotlib.pyplot as plt

def driver():
# Take in constant values
    T_s = -15
    T_i = 20
    alpha = 0.138e-6
    t = 60*24*60*60
# Define the temperature as a function of x
    T = lambda x: T_s + (T_i - T_s)* scipy.special.erf(x/(2*np.sqrt(alpha*t)))

# Define the first derivative of the temperature function
    #Tp = lambda x: (x-2)*(x-5)*np.exp(x)+(2*x-7)*np.exp(x) 

    x = np.arange(0, 1.00, step=0.001)
    T_x = T(x)

    x_ = []
    count = 0

    while (count < len(x)):
        if (T_x >= 0):
            x_ = x_.append(x[count])
            count +=1

    # Function defined over positive values
    T_x_ = T(x_)

    plt.plot (x_, T_x_)
    plt.xlabel('x in meters')
    plt.ylabel('T(x) at t = 60 Days')
    plt.xlim(-10, 10)
    plt.ylim(-20, 20)
    
    plt.show()


driver()