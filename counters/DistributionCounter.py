import math


class DistributionCounter:

    tCounter = None
    meanCounter = None
    varianceCounter = None

    def __init__(self, tCounter, meanCounter, varianceCounter):
        self.tCounter = tCounter
        self.meanCounter = meanCounter
        self.varianceCounter = varianceCounter

    def count(self, data1, data2, k):
        T = self.tCounter.countT(data1, data2, k)
        mean = self.meanCounter.count(data1.getY(), data1.getY())
        variance = math.sqrt(self.varianceCounter.count(data1.getY(), data1.getY(), k))
        #print T
        #print mean
        #print variance
        #return T
        return (T - mean)/variance

