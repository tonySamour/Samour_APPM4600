import numpy as np
import matplotlib.pyplot as plt
import math
import random

# Create driver function for part 1 of 
def driver1():

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

# Second function for part 2

def driver2():

    numCurves = np.linspace(0, 10, num = 11)
    for i in numCurves:
        # Create theta vector from 0 to 2pi
        theta = np.linspace(0, 2*np.pi, num = 1001)
        
        # Assign values to variables given in problem
        R = i
        delr = 0.05
        f = 2 + i
        p = random.uniform(0, 2)

        # Create parametric functions
        x = R*(1+delr*np.sin(f*theta + p))*np.cos(theta)

        y = R*(1+delr*np.sin(f*theta + p))*np.sin(theta)

        # Parametric Plotting Code adapted from Brown Python Tutorial: https://www.cfm.brown.edu/people/dobrush/am33/python/?/p1/parametric.html


        plt.plot(x, y, linewidth=1)

        plt.xlim(-15, 15)
        plt.ylim(-15, 15)
        plt.gca().set_aspect('equal', adjustable='box')
    
    # Plot all at once
    plt.show()


driver1()
driver2()

# Note: I do not know how to get both graphs to plot at the same time