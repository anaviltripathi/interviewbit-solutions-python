class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        m = len(A)
        n = len(A[-1])
        import sys
        cost = [[sys.maxint] * (n+1) for i in range(m+1)]
        cost[0][0] = 0
        for i in range(m):
            for j in range(len(A[i])):
                cost[i+1][j+1] = A[i][j] + min(cost[i][j], cost[i][j+1])

        return min(cost[-1])

