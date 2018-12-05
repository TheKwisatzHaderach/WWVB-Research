import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
from scipy import signal

fs, data = wavfile.read('data/oneminStero.wav') # load the data
a = data.T[1] # this is a two channel soundtrack, I get the first track
b=[(ele/2**16.)*2-1 for ele in a] # this is 16-bit track, b is now normalized on [-1,1)
c = fft(b) # calculate fourier transform (complex numbers list)
d = len(c)/2  # you only need half of the fft list (real signal symmetry)
plt.plot(abs(c[:(d-1)]),'r') 
plt.show()



wwvbSignal = []

def replicaCorrelator(wwvbSignal, Zero, One, X): #Inputs are WWVB Signal and Zero, One, X Replicas
    bitStream = ""
    for i in range(60): #60 Seconds
        #look at 1 second window 60 times
        start = i *44100
        end = (i*44100) + 44100

        #Take Correlation of 1 Second with all 3 replicas
        corrZero = signal.correlate(wwvbSignal[start:end], Zero, mode='full')
        corrOne = signal.correlate(wwvbSignal[start:end], One, mode='full')
        corrX = signal.correlate(wwvbSignal[start:end], X, mode='full')

        #take local max around index 44100
        numZero = int(max(corrZero[44078:44123:1]) / 1000000000)
        numOne = int(max(corrOne[44078:44123:1]) / 1000000000)
        numX = int(max(corrX[44078:44123:1]) / 1000000000)

        if numOne > (numX *2): # we have one or zero
            if numZero > (numOne + (numX * 0.8)):
                bitStream = bitStream + '0'
            else:
                bitStream = bitStream + '1'
        else:
            bitStream = bitStream + 'X'
    return bitStream




