import math


class SineDataGenerator:
    def __init__(self):
        pass

    def generate(self, xes):
        result = []
        for i in range(0, len(xes)):
            val = xes[i]
            result.append(math.sin(val))
        return result
