# Sampling
## Sampled time 
To generate the array that is representing the sampled time the \textit{NumPy} library can be used. This library provides a function \textit{np.arange()}. The array takes three parameters:
- **start**: the start of the interval, the interval will include this value.
- **stop**: the end of the interval, the interval will not include this value. 
- **step**: the spacing between the values. 

```python
import numpy as np
# Sample period
T = 1/1600 
array_sampled_time = np.arange(0, 2+T, T)
print(array_sampled_time)
```

The maximum frequency which can be present in a continuous signal such that the original signal can be reconstructed again from the sampled signal is half the sampling rate. This is according to the Nyquist sampling theorem.  
$f_{max} < f_s/2$    
<br/>
This means that in this case the maximum frequency is 800 Hz. 

## Sampled signal
Creating a sampled version of the function  
$x = 4+2*np.sin(2*\pi*100*t)$
```python
import numpy as np

# Sampling period
T = 1/1600
# Sampled time array
t = np.arange(0, 2, T)
# Function
x = 4+2*np.sin(2*np.pi*100*t)
print(x)
```

# Plot the sampled signal
To plot the signal as a function of time the library matplotlib is used. This library provides functions to plot data into a graph. To plot the sampled signal first the sampling period and the sampling rate are defined. The formula for calculating the sampling period is:  
$T=1/F$
<br/>
Where F is the sampling frequency. The sampling rate is the number of samples per second (fs).  
<br/>
Next the time array and the function are defined and after that the sampled signal is plotted using the matplotlib. The function is plotted using plt.stem() instead of plt.plot() because plt.stem() creates a stem plot what is more effective to display siganls represented as arrays. Where plt.plot() will plot a continuous line between data points on a graph. 
<br/>
```python
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

# Plotting the signal
plt.stem(t,x)
plt.xlabel('Time in seconds')
plt.ylabel('x(t)')
plt.title('Sampled signal')
plt.show()
```

# Frequency spectrum
To plot the double sided frequency spectrum of the sampled sine function a fast Fourier transform is used. A fast Fourier transform is used to convert a signal from the time domain to the frequency domain. The FFT function returns the complex Fast Fourier Transform.  
<br/>
A two-sided frequency spectrum is a representation of the signal including both negative and positive frequencies. The Fourier transform includes both positive and negative frequency components. 
<br/>
To compute the two sided frequency spectrum of the signal the array of frequencies that correspond to the elements of the FFT is created with the function np.fft.fftfreq(). This function takes two arguments, the length of the signal that is calculated with the function len() and the sampling period.  
<br/>
The Fourier transform of a signal returns a complex-value vector to plot this the complex vector needs to be transformed in something that can be plotted. To do this the magnitued squared of the copmlex vector is taken and divided by the length of the input signal to scale it.  
```python
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
```