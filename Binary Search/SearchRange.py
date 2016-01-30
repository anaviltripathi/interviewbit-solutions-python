class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    import copy
    def searchRange(self, A, B):
        start = 0
        end = len(A) - 1
        
        mid = (start + end)/2
        if A[start] > B: return [-1,-1]
        if A[end] < B: return [-1,-1]
        while not(B == A[mid] and B != A[mid-1]):
            if B < A[mid] or (mid > 0 and B == A[mid-1]):
                end = mid
            elif B > A[mid]:
                start = mid
            mid = (start + end) / 2
            if start == end -1 and A[mid] != B:
                return [-1,-1]
            if mid == 0 :
                break
                
                
        
            
        final_start = mid
        
        
        start = 0
        end = len(A) -1
        mid = (start + end )/2
        while B != A[mid] or (mid < len(A) -1 and B == A[mid+1]):
            if A[len(A)-1] == B: 
                mid = len(A) -1 
                break
            if B < A[mid]:
                end = mid
            elif B > A[mid] or (mid < len(A) - 1 and B == A[mid+1]):
                start = mid
            mid = (start + end)/2
            if mid == 0 and B== A[mid]:
                break
            
            if start == end -1 and A[mid] != B:
                return [-1,-1]
        
        
        return [final_start, mid]
        

