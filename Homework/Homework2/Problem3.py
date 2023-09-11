import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0, 1, step=0.01)

y = math.exp(x)
print(y - 1)