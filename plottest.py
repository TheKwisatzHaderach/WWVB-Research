import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

#Use python wave module to open and read in file
spf = wave.open('data/oneminch1.wav','r')

#Extract Raw Audio from Wav File an store in Numpy Array
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')

#plot signal array using matplotlib.pyplot as plt
plt.figure(1)
plt.title('WWVB Time Signal')
plt.plot(signal)

plt.show()



