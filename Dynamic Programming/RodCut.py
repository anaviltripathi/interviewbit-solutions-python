class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def rodCut(self, A, B):
        B = [0] + B + [A]
        from sys import maxint
        n = len(B)
        dp = [[maxint]*(n) for i in range(n)]
        par = [[0]*(n) for i in range(n)]
        
        for i in range(n):
            dp[i][i] = 0
            if i < n - 1:
                dp[i][i+1] = 0
            
        for gap in range(3,len(B)+1):
            for i in range(n-gap+1):
                j = i + gap - 1
                for k in range(i+1, j):
                    if dp[i][k] + dp[k][j] + B[j]-B[i] < dp[i][j]:
                        dp[i][j]= dp[i][k] + dp[k][j] + B[j]-B[i]
                        par[i][j] = k
             

        def make_par(i,j):
            #print res, i , j
            if i == j:
                res.append(B[i])
            elif i == j - 1:
                pass
                #res.append(B[i])
            else:
                k = par[i][j]
                #print k
                res.append(B[k])
                make_par(i,k)
                make_par(k,j)
        
        res = []            
        i = 0
        j = n-1
        
        make_par(i,j)
        return res
                

