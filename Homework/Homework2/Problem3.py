import numpy as np
import matplotlib.pyplot as plt
import math

# (b) Is this algorithm stable?
x = 2
delx = 0.0001

xPert = x + delx

y = math.exp(x) - 1
yPert = math.exp(xPert) - 1

print("Taking in x value", y)
print("Taking in perturbed x value", yPert)

# (c) Take in a small x value. How many correct digits does the algorithm give?

x2 = 9.999999995000000 * 10**-10
y2 = math.exp(x2) - 1

print("(c) ", y2)

# (d) Find a polynomial approx. of f(x) that is accurate to 16 digits for above x value

f = 10**(-9) # Given in part (c)

absError = abs(f - (x2 + (x2**2)/2))
relError = absError/f

print ("(d) Relative error: ", relError)