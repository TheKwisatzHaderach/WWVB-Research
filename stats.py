import statistics 
import sys

sampleZero = [451534543, 354263263, 157104645]
sampleOne = [151534543, 354263263, 357104645]
sampleX = [324263263, 354263263, 387104645]

print("Standard Deviation of sample is % s " % (statistics.stdev(sampleZero))) 
print("Standard Deviation of sample is % s " % (statistics.stdev(sampleOne))) 
print("Standard Deviation of sample is % s " % (statistics.stdev(sampleX))) 