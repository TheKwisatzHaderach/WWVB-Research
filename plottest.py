import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

spf = wave.open('data/sample1ch1.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')


#If Stereo
if spf.getnchannels() == 2:
    print 'Just mono files'
    sys.exit(0)

seconds = []
count = 0
for x in range(0,121):
    seconds.append(count)
    count = count + (44100)

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(signal)
#plt.xlim(0,120)
#plt.xticks(np.linspace(-0,120,120,endpoint=True))
for i in seconds:
    plt.axvline(i, color="red")
plt.text(0,44100,'blah',rotation=90)
plt.show()