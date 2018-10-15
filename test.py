import numpy as np

minutes = 42

#Takes in minutes as integer and returns a binary encoded string (seconds :1 - :8)
def getMinutes(minutes):
    bnum = bin(minutes)
    new = bnum[2:len(bnum)]

    while len(new) < 7:
        new = '0' + new

    print(new)

    new = new[:3] + '0' + new[3:]

    print(new)
    return new

#getMinutes(minutes)

hours = 14

#takes in hours as integer and returns a binary encoded string (seconds :12 - :18)
def getHours(hours):
    bnum = bin(hours)
    new = bnum[2:len(bnum)]

    while len(new) < 6:
        new = '0' + new

    print(new)

    new = new[:2] + '0' + new[2:]

    print(new)
    return new

#getHours(hours)

from scipy import signal
sig = np.repeat([0., 1., 1., 0., 1., 0., 0., 1.], 128)
sig_noise = sig + np.random.randn(len(sig))
corr = signal.correlate(sig_noise, np.ones(128), mode='same') 

print(len(sig))
print(len(sig_noise))
print(len(corr))