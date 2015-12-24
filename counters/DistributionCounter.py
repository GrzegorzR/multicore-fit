import math


class DistributionCounter:

    tCounter = None
    meanCounter = None
    varianceCounter = None

    def __init__(self, tCounter, meanCounter, varianceCounter):
        self.tCounter = tCounter
        self.meanCounter = meanCounter
        self.varianceCounter = varianceCounter

    def count(self, arr1, arr2, k):
        T = self.tCounter.countT(arr1, arr2, k)
        mean = self.meanCounter.count(arr1, arr2)
        variance = math.sqrt(self.varianceCounter.count(arr1, arr2, k))
        #print T
        #print mean
        #print variance
        #return T
        return (T - mean)/variance

