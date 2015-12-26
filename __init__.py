from counters import EucDistanceCounter, TCounter, MeanCounter, VarianceCounter, DistributionCounter
from generators import RandomArrayGenerator, SineDataGenerator, SineWithNoiseGenerator, GaussGenerator
from plotters import DistributionPlotter
import matplotlib.pyplot as plt
import time





def main():
    xgen1 = RandomArrayGenerator.RandomArrayGenerator(-10,10)
    xgen2 = RandomArrayGenerator.RandomArrayGenerator(-10,10)
    gen1 = SineWithNoiseGenerator.SineWithNoiseGenerator(xgen1, 1)
    gen2 = SineWithNoiseGenerator.SineWithNoiseGenerator(xgen1, 0.5)
    #gen2 = SineWithNoiseGenerator.SineWithNoiseGenerator(0)

    d = EucDistanceCounter.EucDistanceCounter(2)
    meanCounter = MeanCounter.MeanCounter()
    varianceCounter = VarianceCounter.VarianceCounter()
    tCounter = TCounter.TCunter(d)
    distributionCounter = DistributionCounter.DistributionCounter(tCounter, meanCounter, varianceCounter)

    distributionPlotter = DistributionPlotter.DistributionPlotter( gen1, gen2, distributionCounter)


    gen11 = GaussGenerator.GaussGenerator(5,5, 1)
    gen12 = GaussGenerator.GaussGenerator(4,4, 1)

    data1 = gen11.generateDataSample(500)
    data2 = gen12.generateDataSample(500)

    plt.plot(data1.getX(), data1.getY(), 'ro')
    plt.plot(data2.getX(), data2.getY(), 'bo')
    plt.show()

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

    distributionPlotter.plot(100, 10, 500)


if __name__ == "__main__":
    main()