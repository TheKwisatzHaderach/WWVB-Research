import matplotlib.pyplot as plt
import numpy as np
import wave
from scipy import signal
import sys
import statistics 

Fs = 44100
f = 1000
ampLow = 200
ampHigh = 6000
hours = 14
minutes = 0

spf = wave.open('data/onehourch1.wav','r')

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
wwvbX = wwvbSignal[4800:48900:1]

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

expectedZero = np.array(createZero(44100,1000, 6000, 200))
expectedOne = np.array(createOne(44100,1000, 6000, 200))
expectedX = np.array(createX(44100,1000, 6000, 200))

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

bitStream = []
templates = [Zero, One, X]
thresholds = [500000000000, 300000000000]
values = ['0', '1', 'X']

#corrects for wwvb offset
print(len(wwvbSignal))
#temp = wwvbSignal[0:4800:1]
wwvbSignal = wwvbSignal[5500::]
wwvbSignal = np.array(wwvbSignal)
#temp = np.array(temp)
#wwvbSignal = np.concatenate((wwvbSignal, temp))
print(len(wwvbSignal))

'''
#works for one minute template
for i in range(59):
    start = i *44100
    end = (i*44100) + 44100
    for x in range(3):
        if x == 2:
            bitStream.append(values[x])
            break
        corr = signal.correlate(wwvbSignal[start:end], templates[x], mode='full')
        if abs(corr[44100]) >= thresholds[x]:
            bitStream.append(values[x])
            break

'''
'''
bitStream = []
devList = []
for i in range(59):
    start = i *44100
    end = (i*44100) + 44100
    corrZero = signal.correlate(nS[start:end], Zero, mode='full')
    corrOne = signal.correlate(nS[start:end], One, mode='full')
    corrX = signal.correlate(nS[start:end], X, mode='full')
    numZero = int(abs(corrZero[44100]) / 1000000000)
    numOne = int(abs(corrOne[44100]) / 1000000000)
    numX = int(abs(corrX[44100]) / 1000000000)

    if numOne > (numX *2): # we have one or zero
        if numZero > (numOne + numX):
            bitStream.append('0')
        else:
            bitStream.append('1')
    else:
        bitStream.append('X')
    #dev = statistics.stdev([numZero, numOne, numX])
    devList.append(numZero)
    devList.append(numOne)
    devList.append(numX)
    devList.append("||")

print(devList)
print(bitStream)
'''
#One min wwvb
bitStream = ""
devList = []
for x in range(59):
    for i in range(60):
        start = (2646000*x) + i * 44100
        end = + ((2646000*x) + (i*44100) ) + 44100

        corrZero = signal.correlate(wwvbSignal[start:end], Zero, mode='full')
        corrOne = signal.correlate(wwvbSignal[start:end], One, mode='full')
        corrX = signal.correlate(wwvbSignal[start:end], X, mode='full')
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
        devList.append(numZero)
        devList.append(numOne)
        devList.append(numX)
        devList.append("||")
    bitStream = bitStream + "----"
    #print(devList)
print(bitStream)

'''

print(devList)


heights = []
#one minute real
for i in range(10,20):
    start = i *44100
    end = (i*44100) + 44100
    for x in range(3):
        corr = signal.correlate(wwvbSignal[start:end], templates[x], mode='full')
        heights.append(abs(corr[44100]))
    heights.append('0')
print(heights)
#sys.exit(0)


#print(bitStream)
plt.figure(1)
plt.title('Expected Signal with AM Modulation (14:00 UTC)')
plt.ylim((-10000, 10000))
plt.xlabel("Sample Rate = 44100Hz | (60 Seconds)")
plt.plot(wwvbSignal)

plt.show()
'''



