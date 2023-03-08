import numpy as np

# Sampling period
T = 1/1600
# Sampled time array
t = np.arange(0, 2, T)
# Function
x = 4+2*np.sin(2*np.pi*100*t)
print(x)