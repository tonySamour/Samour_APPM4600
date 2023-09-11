import numpy as np
import matplotlib.pyplot as plt
import math

# (b) Is this algorithm stable?
x = 2
delx = 0.0001

xPert = x + delx

y = math.exp(x)
yPert = math.exp(xPert)

print("Taking in x value", y - 1)
print("Taking in perturbed x value", yPert - 1)

# (c) Take in a small x value. How many correct digits does the algorithm give?

x2 = 9.999999995000000 * 10**-10
y2 = math.exp(x2)

print("(c) ", y - 1)
