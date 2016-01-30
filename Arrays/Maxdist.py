class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        if len(A) == 1: return 0
        Lmin = [0]*n
        Rmax = [0]*n
        Lmin[0] = A[0]
        for i in range(1,n):
            Lmin[i] = min(Lmin[i-1],A[i])
        Rmax[n-1] = A[n-1]
        for i in range(n-2,-1,-1):
            Rmax[i] = max(Rmax[i+1],A[i])
        
        i = 0
        j = 0
        ret = -1
        if n == 1:
            return ret
        while i < n and j < n:
            if Lmin[i] <= Rmax[j]:
                ret = max(ret, j-i)
                j += 1
            else:
                i += 1
        return ret
        
