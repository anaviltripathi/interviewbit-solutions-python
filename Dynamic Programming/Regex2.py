class Solution:
    # @param s : string
    # @param p : string
    # @return an integer
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[0]*(m+1) for i in range(n+1)]
        dp[0][0] = 1
        for i in xrange(1,n+1):
            x = p[i-1]
            if x == "*" and i > 1:
                dp[i][0] = dp[i-2][0]
            for j in xrange(1, m + 1):
                if x == "*":
                    dp[i][j] = dp[i-2][j] or dp[i-1][j]
                    if p[i-2] == '.' or p[i-2] == s[j-1]:
                        dp[i][j] = dp[i][j] or dp[i][j-1]
                elif x == s[j-1] or x == '.':
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]
                

