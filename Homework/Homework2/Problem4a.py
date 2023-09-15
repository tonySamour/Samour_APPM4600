import numpy as np
import matplotlib.pyplot as plt
import math
import operator

# Create a vector t starting at 0 incrementing by pi/30 to pi
t = np.linspace(0, np.pi, num = 31)

# Create a vector y = cos(t)
y = np.cos(t)

# Write a sum S from k=1 to N, summing the products of t and y
S = 0
# Create an iterating variable k, starting at k=1
k = 0
# Create variable N, the size of t and y
N = len(t)

while k< N:
    S = S + t[k] * y[k]
    k = k + 1

# Print statement to show the value of S
print('The Sum is: ', S)