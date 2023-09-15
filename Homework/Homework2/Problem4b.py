import numpy as np
import matplotlib.pyplot as plt
import math

# Create driver function 
def driver():

    # Create theta vector from 0 to 2pi
    theta = np.linspace(0, 2*np.pi, num = 1001)
    
    # Assign values to variables given in problem
    R = 1.2
    delr = 0.1
    f = 15
    p = 0

    # Create parametric functions
    x = R*(1+delr*np.sin(f*theta + p))*np.cos(theta)

    y = R*(1+delr*np.sin(f*theta + p))*np.sin(theta)

    # Parametric Plotting Code adapted from Brown Python Tutorial: https://www.cfm.brown.edu/people/dobrush/am33/python/?/p1/parametric.html
    plt.plot(x, y, 'g-', linewidth=2)

    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

driver()
