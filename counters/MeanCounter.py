

class MeanCounter:

    def count(self, arrA, arrB):
        na = float(len(arrA))
        nb = float(len(arrB))
        n = na + nb
        nominator = na*(na - 1) + nb*(nb -1)
        denominator = n*(n - 1)
        return nominator/denominator

