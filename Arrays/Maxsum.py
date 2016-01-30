class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_here = A[0]
        res = A[0]
        for x in A[1:]:
            max_here = max(x, max_here + x)
            res = max(max_here, res)
        
        return res
