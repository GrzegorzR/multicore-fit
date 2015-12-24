from counters import EucDistanceCounter, TCounter, MeanCounter
from generators import RandomArrayGenerator, SineDataGenerator, SineWithNoiseGenerator
import matplotlib.pyplot as plt
import time


d = EucDistanceCounter.EucDistanceCounter(2)
randomGenerator = RandomArrayGenerator.RandomArrayGenerator()
sineGenerator = SineDataGenerator.SineDataGenerator()
sinWithNoiseGenerator = SineWithNoiseGenerator.SineWithNoiseGenerator(0.01)
meanCounter = MeanCounter.MeanCounter()

tCounter = TCounter.TCunter(d)

xes = randomGenerator.generate(1000)
xes = sorted(xes)
values = sineGenerator.generate(xes)
noiseValues =sinWithNoiseGenerator.generate(xes)
mhm = tCounter.countT(values, noiseValues, 5)


print xes
print values
print noiseValues
print mhm
print meanCounter.count(values,noiseValues)

plt.interactive(False)
plt.plot(xes, noiseValues)
plt.plot(xes, values)
plt.show()
#time.sleep(100000)
#print d.count(1, 1.2)
