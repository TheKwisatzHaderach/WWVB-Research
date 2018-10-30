import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import wave
import sys

Fs = 44100
f = 1000
ampLow = 200
ampHigh = 6000

spf = wave.open('data/oneminch1.wav','r')

#Extract Raw Audio from Wav File
wwvbSignal = spf.readframes(-1)
wwvbSignal = np.fromstring(wwvbSignal, 'Int16')

testwwvb = wwvbSignal[1460026:1504126:1]
print(len(testwwvb))

def createOne(Fs, f, ampHigh, ampLow):
    second = []
    for lowsample in range(0,22050):
        second.append(ampLow * np.sin(2 * np.pi * f / Fs * lowsample))
    for highsample in range(22050, 44100):
        second.append(ampHigh * np.sin(2 * np.pi * f / Fs * highsample))
    return second

testOne = np.array(createOne(44100,1000, 6000, 200))

corr1 = signal.correlate(testOne, testOne, mode='full')
corr2 = signal.correlate(testwwvb, testOne, mode='full')

plt.figure(1)
plt.title('Expected Signal with AM Modulation')
plt.ylim((-10000, 10000))
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(testOne)


plt.figure(2)
plt.title('WWVB Signal 13th second')
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(testwwvb)


plt.figure(3)
plt.title('Same')
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(corr1)

plt.figure(4)
plt.title('Full')
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(corr2)

plt.show()