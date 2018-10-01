import numpy as np
import wave

spf = wave.open('data/sample1ch1.wav','r')

signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')

print(len(signal)/120)