import matplotlib.pyplot as plt
import numpy as np
import wave
from scipy import signal
import sys

Fs = 44100
f = 1000
ampLow = 200
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

def createZero(Fs, f, ampHigh, ampLow):
    second = []
    for lowsample in range(0,8820):
        second.append(ampLow * np.sin(2 * np.pi * f / Fs * lowsample))
    for highsample in range(8820, 44100):
        second.append(ampHigh * np.sin(2 * np.pi * f / Fs * highsample))
    return second

def createOne(Fs, f, ampHigh, ampLow):
    second = []
    for lowsample in range(0,22050):
        second.append(ampLow * np.sin(2 * np.pi * f / Fs * lowsample))
    for highsample in range(22050, 44100):
        second.append(ampHigh * np.sin(2 * np.pi * f / Fs * highsample))
    return second

def createX(Fs, f, ampHigh, ampLow):
    second = []
    for lowsample in range(0,35280):
        second.append(ampLow * np.sin(2 * np.pi * f / Fs * lowsample))
    for highsample in range(35280, 44100):
        second.append(ampHigh * np.sin(2 * np.pi * f / Fs * highsample))
    return second

def getMinutes(minutes):
    new = ""
    if minutes >= 40:
        new = new + '1'
        minutes = minutes - 40
    else:
        new = new + '0'
    if minutes >= 20:
        new = new + '1'
        minutes = minutes - 20
    else:
        new = new + '0'
    if minutes >= 10:
        new = new + '1'
        minutes = minutes - 10
    else:
        new = new + '0'
    new = new + '0'
    if minutes >= 8:
        new = new + '1'
        minutes = minutes - 8
    else:
        new = new + '0'
    if minutes >= 4:
        new = new + '1'
        minutes = minutes - 4
    else:
        new = new + '0'
    if minutes >= 2:
        new = new + '1'
        minutes = minutes - 2
    else:
        new = new + '0'
    if minutes >= 1:
        new = new + '1'
        minutes = minutes - 11
    else:
        new = new + '0'
    return new

def getHours(hours):
    new = ""
    if hours >= 20:
        new = new + '1'
        hours = hours - 20
    else:
        new = new + '0'
    if hours >= 10:
        new = new + '1'
        hours = hours - 10
    else:
        new = new + '0'
    new = new + '0'
    if hours >= 8:
        new = new + '1'
        hours = hours - 8
    else:
        new = new + '0'
    if hours >= 4:
        new = new + '1'
        hours = hours - 4
    else:
        new = new + '0'
    if hours >= 2:
        new = new + '1'
        hours = hours - 2
    else:
        new = new + '0'
    if hours >= 1:
        new = new + '1'
        hours = hours - 1
    else:
        new = new + '0'
    return new

Zero = createZero(Fs, f, ampHigh, ampLow)
One = createOne(Fs, f, ampHigh, ampLow)
X = createX(Fs, f, ampHigh, ampLow)


minutesS = getMinutes(minutes)
hoursS = getHours(hours)

newSignal = expectedSignal(hoursS, minutesS, Zero, One, X)

#Checks to make sure that wwvbSignal and newSignal are same length
while len(wwvbSignal) > len(newSignal):
    newSignal.append(0)

nS = np.array(newSignal)

#Taking absolute to better visualize
#wwvbSignal = np.absolute(wwvbSignal)
#nS = np.absolute(nS)

corr = signal.correlate(wwvbSignal, nS, mode='full') 

plt.figure(1)
plt.title('Expected Signal with AM Modulation (14:00 UTC)')
plt.ylim((-10000, 10000))
plt.xlabel("Sample Rate = 44100Hz | (60 Seconds)")
plt.plot(nS)

plt.figure(2)
plt.title('WWVB Signal 1 Minute (14:00 UTC)')
plt.xlabel("Sample Rate = 44100Hz | (60 Seconds)")
plt.plot(wwvbSignal)


plt.figure(3)
plt.title('Correlated Signal (14:00 UTC) Taken from WWVB and Expected')
plt.plot(corr)

plt.show()




