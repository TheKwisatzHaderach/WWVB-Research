import matplotlib.pyplot as plt
import numpy as np
import wave
from scipy import signal
import sys

frequency = 44100
ampLow = 3000
ampHigh = 6000
hours = 14
minutes = 0

spf = wave.open('data/oneminch1.wav','r')

#Extract Raw Audio from Wav File
wwvbSignal = spf.readframes(-1)
wwvbSignal = np.fromstring(wwvbSignal, 'Int16')


#Function that generatedd the expected signal
#Everything will remain Constant Exept for Hour and Minute
#Used to create One minute Expected Signals of AM during August 21, 2017
def expectedSignal(hoursS, minutesS, Zero, One, X):
    wwvbExpected = []
    
    wwvbExpected = wwvbExpected + X #0 Second
    for min in minutesS:
        if min == '0':
            wwvbExpected = wwvbExpected + Zero
        else:
            wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + X # 9 Second
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + Zero
    for hour in hoursS:
        if hour == '0':
            wwvbExpected = wwvbExpected + Zero
        else:
            wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + X #19 Second
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + Zero

    #Day of the year 233 :22 - :33
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + X #29 Second

    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + One #36
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + X #39 Second

    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + Zero #44
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + Zero 
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + X #49 Second

    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + Zero #54
    wwvbExpected = wwvbExpected + Zero
    wwvbExpected = wwvbExpected + Zero 
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + One
    wwvbExpected = wwvbExpected + X #59 Second

    return wwvbExpected

def createZero(frequency, ampLow, ampHigh):
    zero = []
    pointtwo = int(0.2 * frequency)
    rest = frequency - pointtwo
    for i in range(0, pointtwo):
        if(i%2 == 0):
            zero.append(ampLow)
        else:
            zero.append(-ampLow)
    for i in range(0, rest):
        if(i%2 == 0):
            zero.append(ampHigh)
        else:
            zero.append(-ampHigh)
    return zero

def createOne(frequency, ampLow, ampHigh):
    one = []
    pointfive = int(0.5 * frequency)
    rest = frequency - pointfive
    for i in range(0, pointfive):
        if(i%2 == 0):
            one.append(ampLow)
        else:
            one.append(-ampLow)
    for i in range(0, rest):
        if(i%2 == 0):
            one.append(ampHigh)
        else:
            one.append(-ampHigh)
    return one

def createX(frequency, ampLow, ampHigh):
    X = []
    pointeight = int(0.8 * frequency)
    rest = frequency - pointeight
    for i in range(0, pointeight):
        if(i%2 == 0):
            X.append(ampLow)
        else:
            X.append(-ampLow)
    for i in range(0, rest):
        if(i%2 == 0):
            X.append(ampHigh)
        else:
            X.append(-ampHigh)
    return X

def getMinutes(minutes):
    bnum = bin(minutes)
    new = bnum[2:len(bnum)]

    while len(new) < 7:
        new = '0' + new

    new = new[:3] + '0' + new[3:]

    return new

def getHours(hours):
    bnum = bin(hours)
    new = bnum[2:len(bnum)]

    while len(new) < 6:
        new = '0' + new

    new = new[:2] + '0' + new[2:]

    return new

Zero = createZero(frequency, ampLow, ampHigh)
One = createOne(frequency, ampLow, ampHigh)
X = createX(frequency, ampLow, ampHigh)

minutesS = getMinutes(minutes)
hoursS = getHours(hours)

newSignal = expectedSignal(minutesS, hoursS, Zero, One, X)

#Checks to make sure that wwvbSignal and newSignal are same length
while len(wwvbSignal) > len(newSignal):
    newSignal.append(0)

print(len(newSignal))
print(len(wwvbSignal))

nS = np.array(newSignal)

corr = signal.correlate(wwvbSignal, newSignal, mode='same')

print(len(corr))

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(corr)
plt.show()



