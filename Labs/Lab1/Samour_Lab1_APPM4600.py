import numpy as np
import matplotlib.pyplot as plt


# 3.1.1 Vectors

# For Lab 2: Creates vectors

x = [1, 2, 3]

x1 = x*3

y = np.array([1,2,3])

y1 = y*3


# 3.1.2 Printing

print ('Here is the vector x: ', x)
# When multiplied by 3, the vector becomes 1, 2, 3, 1, 2, 3, 1, 2, 3
print ('Here is the vector x multiplied by 3: ', x1)

print ('Here is the array y: ', y)
# When multiplied by 3, the array becomes 3 6 9
print ('Here is the array y multiplied by 3: ', y1)


# 3.1.3 Plotting


# For Lab 2: Creates x vector and y formulas

X =np.linspace(0, 2 * np.pi, 100)
Ya = np.sin(X)
Yb = np.cos(X)

# For Lab 2: Plots Ya and Yb against X and shows the plot

plt.plot (X, Ya)
plt.plot (X, Yb)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 3.2 Exercises
# 3.2.1

# For Lab 2: Creating the same vector using two different commands

x2 = np.linspace(0.0, 1.0, num=11, retstep=False)

y2 = np.arange(0.0, 1.1, step=0.1)

print ('First three values of x2: ', x2[0:3])
print ('First three values of y2: ', y2[0:3])

# 3.2.4

w = 10**(-np.linspace(1,10,10))

print('These are the entries of w: ', w)

x3 = np.linspace(1.0, len(w), num=len(w))

s = 3*w

# For Lab 2: Creates plot with log scale on axis

plt.semilogx(x3, w)
plt.semilogx(x3, s)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
