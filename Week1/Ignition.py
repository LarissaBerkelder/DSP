import numpy as np
import matplotlib.pyplot as plt

# Sampling period 
T = 1/1600
# Frequency
fs = 1600
# Sampled time array
t = np.arange(0, 2, T)
# Function 
x = 4+2*np.sin(2*np.pi*100*t)

# Fast Fourier Transform
X = np.fft.fft(x)

# Creating the two sided frequency spectrum 
freqs = np.fft.fftfreq(len(x), d=T)
S = np.abs(X)**2/len(x)

plt.figure()
plt.plot(freqs, S, 'b')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.xlim(-800, 800)
plt.show()