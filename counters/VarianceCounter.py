


class VarianceCounter:


    def count(self,arrA,arrB,k):
        na = float(len(arrA))
        nb = float(len(arrB))
        n = na + nb

        A = 1/(n*k)
        B = (na*nb)/(n*n)
        C = 4*((na*na*nb*nb)/(n*n*n*n))

        return A * (B + C)