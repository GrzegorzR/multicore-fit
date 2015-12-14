
import EucDistanceCounter
import LowestKNumberCounter

class TCunter:

    eucDisCounter = None
    lowestKNumberCounter = LowestKNumberCounter.LowestKNumberCounter()

    def __init__(self, eucDisCounter):
        self.eucDisCounter = eucDisCounter
        pass


    def countT(self, arr1, arr2, k):
        sumT = 0
        for i in range(0, len(arr1)+len(arr2)):
            ithSum = 0
            for i in range(0,k):
                dis1 = map(self.eucDisCounter.count, arr1[i], arr1)
                dis2 = map(self.eucDisCounter.count, arr1[i], arr2)
                print dis1
                print dis2
                tmp  = self.lowestKNumberCounter.isKthLowestNumberInFirstArray(dis1, dis2, k)
                print tmp
                ithSum = ithSum + tmp
            sumT = sumT + ithSum
        nominator = k*(len(arr1)+len(arr2))
        return sumT/nominator

