class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        
        if len(A) == 1:
            return 1 if A[0] < B else 0
        
        if not A:
            return 0
        
        start = 0
        end = len(A) - 1
        
        while start < end:
            mid = (start + end) /2

            if A[mid] < B:
                start = mid + 1
                #print start
            elif A[mid] > B:
                end = mid
            else:
                return mid
          
        return start + 1 if start == len(A) - 1 else start

