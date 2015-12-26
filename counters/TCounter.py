
import EucDistanceCounter
import LowestKNumberCounter

class TCunter:

    eucDisCounter = None
    lowestKNumberCounter = LowestKNumberCounter.LowestKNumberCounter()

    def __init__(self, eucDisCounter):
        self.eucDisCounter = eucDisCounter
        pass


    def countT(self, data1, data2, k):
        sumT = 0
        xArr1 = data1.getX()
        arr1 = data1.getY()

        xArr2 = data2.getX()
        arr2 = data2.getY()

        for i in range(0, len(arr1)):
            ithSum = 0
            dis1 = self.eucDisCounter.countArr(arr1[i], xArr1[i], xArr1, arr1)
            dis2 = self.eucDisCounter.countArr(arr1[i], xArr1[i], xArr2, arr2)
            for j in range(1, k+1):
                #print dis1
                #print dis2
                tmp  = self.lowestKNumberCounter.isKthLowestNumberInFirstArray(dis1, dis2, j)
                #print tmp
                ithSum = ithSum + tmp
            sumT = sumT + ithSum
        for i in range(0, len(arr2)):
            ithSum = 0
            dis1 = self.eucDisCounter.countArr(arr2[i], xArr2[i], xArr1, arr1)
            dis2 = self.eucDisCounter.countArr(arr2[i], xArr2[i], xArr2, arr2)
            for j in range(1, k+1):
                #print dis1
                #print dis2
                tmp  = self.lowestKNumberCounter.isKthLowestNumberInFirstArray(dis2, dis1, j)
                #print tmp
                ithSum = ithSum + tmp
            sumT = sumT + ithSum
        #print sumT
        nominator = k*(len(arr1)+len(arr2))
        #print nominator
        return float(sumT)/float(nominator)

