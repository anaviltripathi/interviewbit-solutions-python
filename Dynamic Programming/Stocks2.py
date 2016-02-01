class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) < 1: return 0
        mProfit = 0
        totalProfit = 0
        for i in range(1,len(A)):
            if A[i] > A[i-1]:
                mProfit += A[i] - A[i-1]
            else:
                totalProfit += mProfit
                mProfit = 0
        totalProfit += mProfit  
        return totalProfit

