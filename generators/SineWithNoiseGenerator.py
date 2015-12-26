import math
import random
from data import DataSample


class SineWithNoiseGenerator:
    noiseVal = None
    randXGen = None

    def __init__(self, randXGen, noiseVal=0.1):
        self.noiseVal = noiseVal
        self.randXGen = randXGen

    def generateDataSample(self, length):
        xes = self.randXGen.generate(length)
        yes = self.generate(xes)
        return DataSample.DataSample(xes, yes)

    def generate(self, xes):
        result = []
        for i in range(0, len(xes)):
            x = xes[i]
            val = math.sin(x) + random.uniform(-self.noiseVal, self.noiseVal)
            result.append(val)
        return result
