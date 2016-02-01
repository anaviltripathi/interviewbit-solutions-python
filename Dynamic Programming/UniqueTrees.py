class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        fact_2n = 1
        fact_n = 1
        import sys
        for i in range(A+2, 2*A + 1):
            fact_2n *= i
            fact_n *= (i-A)
        return fact_2n / fact_n if fact_2n / fact_n < sys.maxint else -sys.maxint -1

