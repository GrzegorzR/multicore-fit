import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy

class DistributionPlotter:
    gen1 = None
    gen2 = None
    disCounter = None

    def __init__(self,gen1, gen2, disCounter):

        self.gen1 = gen1
        self.gen2 = gen2
        self.disCounter = disCounter

    def plot(self, arrLen, k, iterations):
        disArr = []
        for i in range(0, iterations):
            print i
            data1 = self.gen1.generateDataSample(arrLen)
            data2 = self.gen2.generateDataSample(arrLen)
            result = self.disCounter.count(data1, data2, k)
            disArr.append(result)
        n, bins, patches = plt.hist(disArr, 20, normed=1, facecolor='green', alpha=0.75)

        sigma = numpy.std(bins)
        mean = sum(bins) / float(len(bins))

        y = mlab.normpdf(bins, mean, sigma)
        l = plt.plot(bins, y, 'r--', linewidth=1)
        #plt.plot(bins)
        plt.show()

