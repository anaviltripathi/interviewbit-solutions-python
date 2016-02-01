class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        m = len(A)
        n = len(A[0])
        dp = [[0]* n for i in range(m)]
        
        if A[0][0] == 1 or A[-1][-1] == 1: return 0
        
        dp[0][0] = 1
        
        for i in range(1,m):
            if A[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0
        
        for j in range(1,n):
            if A[0][j] == 0:
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = 0
                
        for i in range(1,m):
            for j in range(1,n):
                if A[i][j] == 0:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = 0
                    
                    
        return dp[-1][-1]

