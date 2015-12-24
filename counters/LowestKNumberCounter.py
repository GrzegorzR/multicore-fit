

class LowestKNumberCounter:

    def __init__(self):
        pass

    def isKthLowestNumberInFirstArray(self,arr1,arr2,k):
        tmp = arr1 + arr2
        tmp = sorted(tmp)
        kthlowest = tmp[k]
        if kthlowest in arr2:
            return 0
        elif kthlowest in arr1:
            return 1