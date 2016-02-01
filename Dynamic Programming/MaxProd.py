class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        if not A:
            return 0
        premax, premin = A[0], A[0]
        res = A[0]
        for n in A[1:]:
            minhere = min(premax*n, premin*n, n)
            maxhere = max(premin*n, premax*n, n)
            res = max(minhere, maxhere,res)
            premin = minhere
            premax = maxhere
            
        return res

