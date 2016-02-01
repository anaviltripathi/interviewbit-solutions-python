class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        if not A: return 0
        n = len(A)
        
        ways = [0] * n
        ways[0] = 1
        
        if A[0] == '0': return 0
        for i in range(1,n):
            if int(A[i]) == 0:
                if int(A[i-1]) == 1 or int(A[i-1]) == 2:
                    ways[i] = max(ways[i-2],1)
                else:
                    return 0
            else:
                if 1 <= int(A[i-1]) <= 2:
                    if int(A[i-1]) == 2 and int(A[i]) < 7:
                        ways[i] = max(ways[i-2],1)
                    elif int(A[i-1]) == 1:
                        ways[i] =  max(ways[i-2],1)
                ways[i] += ways[i-1]

        return ways[-1]
            
        
        

