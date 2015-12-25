import matplotlib.pyplot as plt


class DistributionPlotter:
    xgen = None
    gen1 = None
    gen2 = None
    disCounter = None

    def __init__(self, xgen, gen1, gen2, disCounter):
        self.xgen = xgen
        self.gen1 = gen1
        self.gen2 = gen2
        self.disCounter = disCounter

    def plot(self, arrLen, k, iterations):
        disArr = []
        for i in range(0, iterations):
            print i
            xes = self.xgen.generate(arrLen)
            arr1 = self.gen1.generate(xes)
            arr2 = self.gen2.generate(xes)
            result = self.disCounter.count(xes, arr1, arr2, k)
            disArr.append(result)
        n, bins, patches = plt.hist(disArr, 20, normed=1, facecolor='green', alpha=0.75)

        #plt.plot(bins)
        plt.show()

