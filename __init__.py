from counters import EucDistanceCounter, TCounter, MeanCounter, VarianceCounter, DistributionCounter
from generators import RandomArrayGenerator, SineDataGenerator, SineWithNoiseGenerator
from plotters import DistributionPlotter
import matplotlib.pyplot as plt
import time



xgen = RandomArrayGenerator.RandomArrayGenerator()
gen1 = SineWithNoiseGenerator.SineWithNoiseGenerator(0.05)
gen2 = SineWithNoiseGenerator.SineWithNoiseGenerator(0.05)
#gen2 = SineWithNoiseGenerator.SineWithNoiseGenerator(0)

d = EucDistanceCounter.EucDistanceCounter(2)
meanCounter = MeanCounter.MeanCounter()
varianceCounter = VarianceCounter.VarianceCounter()
tCounter = TCounter.TCunter(d)
distributionCounter = DistributionCounter.DistributionCounter(tCounter, meanCounter, varianceCounter)

distributionPlotter = DistributionPlotter.DistributionPlotter(xgen , gen1, gen2, distributionCounter)





#mhm = tCounter.countT(values, noiseValues, 5)

"""
print xes
print values
print noiseValues
#print mhm
print distributionCounter.count( values, noiseValues, 5)

plt.interactive(False)
plt.plot(xes, noiseValues)
plt.plot(xes, values)
plt.show()
#time.sleep(100000)
#print d.count(1, 1.2)
"""

distributionPlotter.plot(100, 5, 100)
