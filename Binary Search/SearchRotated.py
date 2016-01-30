class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        
        if len(A) == 1:
            return 1 if A[0] == B else 0
        
        i = 1
        start = 0
        end = len(A) - 1
        
        while A[start] > A[end]:
            mid = (start + end) / 2
            #print mid
            if A[mid] < A[start]:
                end = mid
            elif A[mid] > A[end]:
                start = mid + 1
            
        actual_start = start
        
        if actual_start != 0:
            if A[actual_start - 1] > B and A[0] < B:
                start = 0
                end = actual_start -1
            elif A[actual_start - 1] < B:
                return 0
            else:
                start = actual_start
                end = len(A) - 1
        else:
            start = 0
            end = len(A) - 1
            
        
        while start < end:
            mid = (start + end) /2
            
            if A[mid] < B:
                start = mid + 1
            elif A[mid] > B:
                end = mid
            else:
                return mid
                
        
        return end if A[end] == B else -1
                
                
        
            
            

