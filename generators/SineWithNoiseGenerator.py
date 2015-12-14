import math
import random


class SineWithNoiseGenerator:

    noiseVal = None

    def __init__(self, noiseVal = 0.1):
        self.noiseVal = noiseVal
        pass

    def generate(self, xes):
        result = []
        for i in range(0, len(xes)):
            x = xes[i]
            val = math.sin(x)+random.uniform(-self.noiseVal, self.noiseVal)
            result.append(val)
        return result