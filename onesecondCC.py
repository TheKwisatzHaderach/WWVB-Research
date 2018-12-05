import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import wave
import sys

SR = 44100
f = 1000
ampLow = 200
ampHigh = 6000

spf = wave.open('data/oneminch1.wav','r')

#Extract Raw Audio from Wav File
wwvbSignal = spf.readframes(-1)
wwvbSignal = np.fromstring(wwvbSignal, 'Int16')

#5th Second (BPSK 0) (Working CC)
wwvbZero = wwvbSignal[182000:226100:1]

#3rd Second (BPSK 1)
#wwvbZeroB = wwvbSignal[93800:137900:1]

#34th Second (BPSK Unsure) (Working CC)
wwvbOne = wwvbSignal[1460026:1504126:1] 

#1rst Second (BPSK 0) (Working CC)
wwvbX = wwvbSignal[(44100 * 6) + 5500:(44100 * 7) + 5500:1]


#Creating One Second Replicas
def createZero(SR, f, ampHigh, ampLow):
    second = []
    for lowsample in range(0,8820):
        second.append(ampLow * np.sin(2 * np.pi * f / SR * lowsample))
    for highsample in range(8820, 44100):
        second.append(ampHigh * np.sin(2 * np.pi * f / SR * highsample))
    return second

def createOne(SR, f, ampHigh, ampLow):
    second = []
    for lowsample in range(0,22050):
        second.append(ampLow * np.sin(2 * np.pi * f / SR * lowsample))
    for highsample in range(22050, 44100):
        second.append(ampHigh * np.sin(2 * np.pi * f / SR * highsample))
    return second

def createX(SR, f, ampHigh, ampLow):
    second = []
    for lowsample in range(0,35280):
        second.append(ampLow * np.sin(2 * np.pi * f / SR * lowsample))
    for highsample in range(35280, 44100):
        second.append(ampHigh * np.sin(2 * np.pi * f / SR * highsample))
    return second

expectedZero = np.array(createZero(44100,1000, 6000, 200))
expectedOne = np.array(createOne(44100,1000, 6000, 200))
expectedX = np.array(createX(44100,1000, 6000, 200))

#Taking absolute to better visualize
#expectedZero = np.absolute(expectedZero)
#expectedOne = np.absolute(expectedOne)
#expectedX = np.absolute(expectedX)
#wwvbZero = np.absolute(wwvbZero)
#wwvbOne = np.absolute(wwvbOne)
#wwvbX = np.absolute(wwvbX)

corr1 = signal.correlate(wwvbZero, expectedZero, mode='full')
corr2 = signal.correlate(wwvbZero, expectedOne, mode='full')
corr3 = signal.correlate(wwvbZero, expectedX, mode='full')

print(corr1[44100])

corr4 = signal.correlate(wwvbOne, expectedZero, mode='full')
corr5 = signal.correlate(wwvbOne, expectedOne, mode='full')
corr6 = signal.correlate(wwvbOne, expectedX, mode='full')

print(corr5[44100])

corr7 = signal.correlate(wwvbX, expectedZero, mode='full')
corr8 = signal.correlate(wwvbX, expectedOne, mode='full')
corr9 = signal.correlate(wwvbX, expectedX, mode='full')

print(corr9[44100])

print(np.argmax(corr1))
print(np.argmax(corr5))
print(np.argmax(corr9))

'''
plt.figure(1)
plt.title('Expected Signal Zero with AM Modulation')
#plt.ylim((-10000, 10000))
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(corr1)


plt.figure(2)
plt.title('WWVB Signal Zero 5th second')
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(corr2)

plt.figure(3)
plt.title('Correlated WWVB Zero With Expected Zero')
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(corr3)

'''

plt.figure(4)
plt.title('Expected Signal with AM Modulation')
#plt.ylim((-10000, 10000))
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(corr4)


plt.figure(5)
plt.title('WWVB Signal 13th second')
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(wwvbSignal[5800::])
print(np.argmax(corr5))

plt.figure(6)
plt.title('Correlated WWVB One with Expected One')
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(wwvbX)



plt.figure(7)
plt.title('Expected Signal X with AM Modulation')
#plt.ylim((-10000, 10000))
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(corr7)

plt.figure(8)
plt.title('WWVB Signal X 1rst second')
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(corr8)

plt.figure(9)
plt.title('Correlated WWVB X with Expected X')
plt.xlabel("Sample Rate = 44100Hz | (1 Seconds)")
plt.plot(corr9)


plt.show()