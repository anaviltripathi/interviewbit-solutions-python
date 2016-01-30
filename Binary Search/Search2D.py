class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        
        start = 0
        end = (len(A) * len(A[0])) -1
        
        m = len(A)
        n = len(A[0])
        
        while start < end:
            mid = (start + end) / 2
            mid_i = mid / n
            mid_j = mid % n
            if A[mid_i][mid_j] < B:
                start = mid + 1
            elif A[mid_i][mid_j] > B:
                end = mid
            else:
                return 1
        
        return 1 if A[-1][-1] == B else 0
        
        
