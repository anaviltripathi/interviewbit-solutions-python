class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        nZero = 0
        l, r = 0, 0
        maxLen = -1
        while r < len(A):
            if nZero <= B:
                if A[r] == 0:
                    nZero += 1
                r += 1
            if nZero > B:
                if A[l] == 0:
                    nZero -= 1
                l += 1
            
            if maxLen < r - l + 1:
                start = l 
                end = r
                maxLen = r - l + 1
            
        
        return range(start, end)


