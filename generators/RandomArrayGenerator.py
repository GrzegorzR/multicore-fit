import random


class RandomArrayGenerator:
    maxV = None
    minV = None


    def __init__(self,minV=-10,maxV=10):
        self.minV = minV
        self.maxV = maxV

    def generate(self,n):
        result = []
        for i in range(0,n):
            result.append(random.uniform(self.minV,self.maxV))
        return result