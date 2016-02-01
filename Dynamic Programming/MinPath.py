class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        if not A: return 0
        m = len(A)
        n = len(A[0])
        import sys
        cost = [ [sys.maxint]* (n+1) for i in range(m+1) ]
        cost[0][1] = 0
        cost[1][0] = 0
        for i in range(m):
            for j in range(n):
                cost[i+1][j+1] = A[i][j] + min(cost[i][j+1], cost[i+1][j])
                
        return cost[-1][-1]
        
