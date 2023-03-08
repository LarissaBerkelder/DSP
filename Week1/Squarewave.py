import numpy as np
import matplotlib.pyplot as plt

# Frequency
fs = 1000
T= fs*2
t = np.linspace(0, 0.5, T) 

x = 2 * np.sign(np.sin(2*np.pi*50*t))


plt.plot(t,x)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('50 Hz Square Waveform')
plt.show()