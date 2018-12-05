import numpy as np 
import matplotlib.pyplot as plt

Fs = 44100
f = 1000
ampHigh = 6000
ampLow = 200

def createZero(Fs, f, ampHigh, ampLow):
    second = []
    for lowsample in range(0,8820):
        second.append(ampLow * np.sin(2 * np.pi * f / Fs * lowsample))
    for highsample in range(8820, 44100):
        second.append(ampHigh * np.sin(2 * np.pi * f / Fs * highsample))
    return second

def createOne(Fs, f, ampHigh, ampLow):
    second = []
    for lowsample in range(0,22050):
        second.append(ampLow * np.sin(2 * np.pi * f / Fs * lowsample))
    for highsample in range(22050, 44100):
        second.append(ampHigh * np.sin(2 * np.pi * f / Fs * highsample))
    return second

def createX(Fs, f, ampHigh, ampLow):
    second = []
    for lowsample in range(0,35280):
        second.append(ampLow * np.sin(2 * np.pi * f / Fs * lowsample))
    for highsample in range(35280, 44100):
        second.append(ampHigh * np.sin(2 * np.pi * f / Fs * highsample))
    return second

Zero = np.array(createZero(Fs, f, ampHigh, ampLow))
One = np.array(createOne(Fs, f, ampHigh, ampLow))
X = np.array(createX(Fs, f, ampHigh, ampLow))


plt.figure(1)
plt.plot(Zero)

plt.figure(2)
plt.plot(One)

plt.figure(3)
plt.plot(X)

plt.show()
