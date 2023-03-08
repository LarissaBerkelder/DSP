import numpy as np
# Sample period
T = 1/1600 
# Time in seconds
time = 2
# Generating the array
array_sampled_time = np.arange(0, time, T)
# Printing the array
print(array_sampled_time)