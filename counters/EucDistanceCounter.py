import math


class EucDistanceCounter:

    D = 2

    def __init__(self,D):
        self.D =D

    def count(self,x1,y1,x2,y2):
        sum = math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)
        return math.sqrt(sum)

    def count1dim(self,x1,x2):
        sum = 0
        for i in range(0,self.D,1):
            tmp = math.pow(x1, i+1) - math.pow(x2, i+1)
            sum = sum + math.pow(tmp, 2)
        return math.sqrt(sum)

    def countArr(self,x1,arr):
        result = []
        for i in range(0,len(arr),1):
            result.append(self.count(arr[i],x1))
        return result
    def countArr(self, x, y, arrX, arrY):
        result = []
        for i in range(0, len(arrX), 1):
            result.append(self.count(x, y, arrX[i], arrY[i]))
        return result

    def setD(self,D):
        self.D = D