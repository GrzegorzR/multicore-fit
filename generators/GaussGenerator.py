import random
from data import DataSample

class GaussGenerator:
    x = None
    y = None
    sigma = None

    def __init__(self, x, y, sigma):
        self.x = x
        self.y = y
        self.sigma = sigma

    def generateDataSample(self, length):
        xarr = []
        yarr = []

        for i in range (0,length):
            xarr.append(random.gauss(self.x, self.sigma))
            yarr.append(random.gauss(self.y, self.sigma))

        return DataSample.DataSample(xarr, yarr)