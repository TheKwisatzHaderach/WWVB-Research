import numpy as np

minutes = 42

#Takes in minutes as integer and returns a binary encoded string (seconds :1 - :8)
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

#getMinutes(minutes)

hours = 14

#takes in hours as integer and returns a binary encoded string (seconds :12 - :18)
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

getHours(hours)

'''
from scipy import signal
sig = np.repeat([0., 1., 1., 0., 1., 0., 0., 1.], 128)
sig_noise = sig + np.random.randn(len(sig))
corr = signal.correlate(sig_noise, np.ones(128), mode='same') 

print(len(sig))
print(len(sig_noise))
print(len(corr))
'''