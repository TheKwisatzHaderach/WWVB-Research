# This is a test of the scipy.signal.correlate example code

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

sig = np.repeat([0., 1., 1., 0., 1., 0., 0., 1.], 128)
sig_noise = sig + np.random.randn(len(sig))
corr = signal.correlate(sig_noise, np.ones(128), mode='same') / 128

seconds = []
count = 64
for x in range(0,8):
    seconds.append(count)
    count = count + (128)

plt.figure(1)
plt.title('Original Signal')
plt.plot(sig)
plt.axhline(y=0.5, linewidth=1, color='g')
for i in seconds:
    plt.axvline(i, color="red")

plt.figure(2)
plt.title('Signal With Noise')
plt.plot(sig_noise)
plt.axhline(y=0.5, linewidth=1, color='g')
for i in seconds:
    plt.axvline(i, color="red")

plt.figure(3)
plt.title('Cross-correlated with a Recatangular Pulse')
plt.plot(corr)
plt.axhline(y=0.5, linewidth=1, color='g')
for i in seconds:
    plt.axvline(i, color="red")


plt.show()
