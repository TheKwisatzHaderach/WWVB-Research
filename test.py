import numpy as np 
import matplotlib.pyplot as plt

Fs = 44100
f = 1000
ampHigh = 6000
ampLow = 200

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

Zero = np.array(createZero(Fs, f, ampHigh, ampLow))
One = np.array(createOne(Fs, f, ampHigh, ampLow))
X = np.array(createX(Fs, f, ampHigh, ampLow))


plt.figure(1)
plt.plot(Zero)

plt.figure(2)
plt.plot(One)

plt.figure(3)
plt.plot(X)

plt.show()




'''
import matplotlib.pyplot as plt
import numpy as np

frequency = 44100
ampLow = 400
ampHigh = 6000



def createZero(frequency, ampLow, ampHigh):
    zero = []
    pointtwo = int(0.2 * (frequency/1000))
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


def interpolatedArray():
    Array = []
    freq = 1000
    for i in range(freq):
        #amplLow = 400
        ampHigh = 6000
        Array.append(ampHigh)
        for x in range(1,21):
            Array.append(ampHigh - (545 * x))
        Array.append(-ampHigh)
        for x in range(1, 22):
            Array.append(-ampHigh + (545 * x))
    return Array
        
test = interpolatedArray()
testNP = np.array(test)
testamp = np.sin(testNP)

time = np.arange(0, 10, 0.1)
amplitude = 800 * np.sin(time)

print(len(amplitude))
print(len(time))

plt.plot(time, amplitude)
plt.title('Sine wave')
plt.show()


'''