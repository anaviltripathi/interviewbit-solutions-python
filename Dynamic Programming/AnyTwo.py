class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        dp = [[0] * (len(A)+1) for _ in range(len(A)+1) ]
        for i in range(len(A)):
            for j in range(len(A)):
                if i == j:
                    dp[i][j] = max(dp[i-1][j] ,dp[i][j-1])
                else:
                    if A[i] == A[j]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j] ,dp[i][j-1])
                if dp[i][j] >= 2:
                    return 1
        return 0

