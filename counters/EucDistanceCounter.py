import math


class EucDistanceCounter:

    D = 2

    def __init__(self,D):
        self.D =D

    def count(self,x1,x2):
        sum = 0
        for i in range(0,self.D,1):
            tmp = math.pow(x1, i+1) - math.pow(x2, i+1)
            sum = sum + math.pow(tmp, 2)
        return math.sqrt(sum)

    def count(self,x1,x2):
        sum = 0
        for i in range(0,self.D,1):
            tmp = math.pow(x1, i+1) - math.pow(x2, i+1)
            sum = sum + math.pow(tmp, 2)
        return math.sqrt(sum)

     def count(self,x1,x2):
        sum = 0
        for i in range(0,self.D,1):
            tmp = math.pow(x1, i+1) - math.pow(x2, i+1)
            sum = sum + math.pow(tmp, 2)
        return math.sqrt(sum)

    def setD(self,D):
        self.D = D