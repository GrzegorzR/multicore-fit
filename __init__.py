from counters import EucDistanceCounter, TCounter, MeanCounter, VarianceCounter, DistributionCounter
from generators import RandomArrayGenerator,  SineWithNoiseGenerator, GaussGenerator
from plotters import DistributionPlotter
import matplotlib.pyplot as plt
import time


def main():
    #plotGaussData     (2, 2, 2, 2, 1, 1, 1000)
    #gaussDataHistogram(2, 2, 2, 2, 1, 1, 100, 200)

    #plotSineData(0.5, 0.1, 1000)
    sineDataHistogram(0.1, 0.1, 100, 200)


def plotSineData(noise1, noise2, arrLen):
    gen1, gen2 = prepareSineGenerators(noise1, noise2)
    plotData(gen1, gen2, arrLen)

def plotGaussData(x1, y1, x2, y2, sigma1, sigma2, arrLen):
    gen1, gen2 = prepareGaussGenerators(x1, y1, x2, y2, sigma1, sigma2)
    plotData(gen1, gen2, arrLen)

def sineDataHistogram(noise1, noise2, arrLen, iterations):
    gen1, gen2 = prepareSineGenerators(noise1, noise2)
    plotResultHisogram(gen1, gen2, arrLen, iterations)

def gaussDataHistogram(x1, y1, x2, y2, sigma1, sigma2, arrLen, iterations):
    gen1, gen2 = prepareGaussGenerators(x1, y1, x2, y2, sigma1, sigma2)
    plotResultHisogram(gen1, gen2, arrLen, iterations)




def prepareSineGenerators(noise1, noise2):
    xgen1 = RandomArrayGenerator.RandomArrayGenerator(-10, 10)
    gen1 = SineWithNoiseGenerator.SineWithNoiseGenerator(xgen1, noise1)
    gen2 = SineWithNoiseGenerator.SineWithNoiseGenerator(xgen1, noise2)
    return gen1, gen2

def prepareGaussGenerators(x1, y1, x2, y2, sigma1, sigma2):
    gen1 = GaussGenerator.GaussGenerator(x1, y1, sigma1)
    gen2 = GaussGenerator.GaussGenerator(x2, y2, sigma2)
    return gen1, gen2

def plotData(gen1, gen2, arrLen):
    data1 = gen1.generateDataSample(arrLen)
    data2 = gen2.generateDataSample(arrLen)

    plt.plot(data1.getX(), data1.getY(), 'ro')
    plt.plot(data2.getX(), data2.getY(), 'bo')
    plt.show()

def plotResultHisogram(gen1, gen2, arrLen, iterations):
    distributionCounter = prepareDistributionCounter()
    distributionPlotter = DistributionPlotter.DistributionPlotter(gen1, gen2, distributionCounter)
    distributionPlotter.plot(arrLen, 10, iterations)


def prepareDistributionCounter():
    d = EucDistanceCounter.EucDistanceCounter(2)
    meanCounter = MeanCounter.MeanCounter()
    varianceCounter = VarianceCounter.VarianceCounter()
    tCounter = TCounter.TCunter(d)
    return DistributionCounter.DistributionCounter(tCounter, meanCounter, varianceCounter)




if __name__ == "__main__":
    main()