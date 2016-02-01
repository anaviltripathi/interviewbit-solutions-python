class Solution:
    # @param S : string
    # @param T : string
    # @return an integer
    def numDistinct(self, S, T):
        n = len(S)
        m = len(T)
        dp = [[0]*(m+1) for i in range(2)]
        dp[0][0] = 1
        dp[1][0] = 1
        for i in range(1,n+1):
            for j in range(1, m+1):
                if S[i-1] == T[j-1]:
                    dp[1][j] += dp[0][j-1]
            dp[0][:] = dp[1][:]
            
        return dp[1][-1]

