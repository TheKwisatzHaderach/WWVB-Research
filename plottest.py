import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

spf = wave.open('data/oneminch1.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')

print(len(signal))


#If Stereo
if spf.getnchannels() == 2:
    print 'Just mono files'
    sys.exit(0)

seconds = []
count = 5580
for x in range(0,60):
    seconds.append(count)
    count = count + (44100)

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(signal)
for i in seconds:
    plt.axvline(i, color="red")
plt.show()


