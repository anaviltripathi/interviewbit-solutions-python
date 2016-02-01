class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        '''
        if not A:
            return 0
            
        dp = [0]*len(A)
        currprofit = -A[0]
        totalprofit = 0
        smallest = A[0]
        for i,price in enumerate(A):
            if price < smallest:
                smallest = price
            currprofit = price - smallest
            totalprofit = max(currprofit, totalprofit)
            dp[i] = totalprofit
            
        currprofit = 0
        totalprofit = 0
        highest = A[-1]
        res = 0
        for i in range(len(A) -1, -1, -1):
            if A[i] > highest: highest = A[i]
            currprofit = highest - A[i]
            totalprofit = max(currprofit , totalprofit)
            res = max(res, totalprofit + dp[i])
        
        return res
        '''
        if not A:
            return 0
        buy1, sell1, buy2, sell2 = -A[0], 0, -A[0], 0
        
        for n in A:
            sell2 = max(sell2, buy2 + n)
            buy2 = max(buy2, sell1 - n)
            sell1 = max(sell1, buy1 + n)
            buy1 = max(buy1, -n)
        
        return sell2
            

