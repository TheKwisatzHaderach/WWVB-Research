import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import wave
import sys

Fs = 44100
f = 1000
ampLow = 200
ampHigh = 6000

hours = 14
minutes = 0

seconds = 60

spf = wave.open('data/oneminch1.wav','r')

#Extract Raw Audio from Wav File
wwvbSignal = spf.readframes(-1)
wwvbSignal = np.fromstring(wwvbSignal, 'Int16')

#1 Second
#wwvbSignalNine = wwvbSignal[48900:93000:1]
#wwvbSignalNine = wwvbSignal[93000:137100:1]

#2 Second (2-3 which are BSPK 0 and 1)
wwvbSignalNine = wwvbSignal[48900:137100:1]

#2 Second (11-12 which are BSPK 0 and 0)
#wwvbSignalNine = wwvbSignal[489900:578000:1]

#2 Second (3-4 which are BSPK 1 and 1)
#wwvbSignalNine = wwvbSignal[93000:181200:1]

#9 Seconds
#wwvbSignalNine = wwvbSignal[4800:401700:1]

def createExpected(Fs, f, ampHigh, ampLow, seconds): #0.2: 8820, 0.5: 22500, 0.8: 35280
    expectedWWVB = []
    for lowsample in range(0,8820):
        expectedWWVB.append(ampLow * np.sin(2 * np.pi * f / Fs * lowsample))
    for highsample in range(8820, 44100):
        expectedWWVB.append(ampHigh * np.sin(2 * np.pi * f / Fs * highsample))

    for lowsample in range(0,8820):
        expectedWWVB.append(ampLow * np.sin(2 * np.pi * f / Fs * lowsample))
    for highsample in range(8820, 44100):
        expectedWWVB.append(ampHigh * np.sin(2 * np.pi * f / Fs * highsample))


    '''
    for i in range(1, 9):
        for lowsample in range(i * 44100, i * 44100 + 8820):
            expectedWWVB.append(ampLow * np.sin(2 * np.pi * f / Fs * lowsample))
        for highsample in range(i * 44100 + 8820, 44100 * (i+1)):
            expectedWWVB.append(ampHigh * np.sin(2 * np.pi * f / Fs * highsample))
    '''

    return expectedWWVB

expectedSignal = createExpected(Fs,f, ampHigh, ampLow, seconds)
print(len(expectedSignal))
esignal = np.array(expectedSignal)

corr = signal.correlate(wwvbSignalNine, esignal, mode='full')

plt.figure(1)
plt.title('Expected 9 seconds')
plt.plot(esignal)

plt.figure(2)
plt.title('WWVB 9 seconds')
plt.plot(wwvbSignalNine)

plt.figure(3)
plt.title('Correlated')
plt.plot(corr)
plt.show()