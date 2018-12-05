import time
import numpy as np
from scipy import signal
import wave


def createZero(Fs, f, ampHigh, ampLow):
    second = []
    for lowsample in range(0,8820):
        second.append(ampLow * np.sin(2 * np.pi * f / Fs * lowsample))
    for highsample in range(8820, 44100):
        second.append(ampHigh * np.sin(2 * np.pi * f / Fs * highsample))
    return second

spf = wave.open('data/oneminch1.wav','r')

#Extract Raw Audio from Wav File
wwvbSignal = spf.readframes(-1)
wwvbSignal = np.fromstring(wwvbSignal, 'Int16')

#5th Second (BPSK 0) (Working CC)
wwvbZero = wwvbSignal[182000:226100:1]

expectedZero = np.array(createZero(44100,1000, 6000, 200))

start_time = time.time()
corr = signal.correlate(wwvbZero, expectedZero, mode='full')
print("My program took", time.time() - start_time, "to run")


print(44100 * (time.time() - start_time))
