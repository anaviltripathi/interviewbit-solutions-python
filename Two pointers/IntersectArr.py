class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        inter = []
        j = 0
        i= 0
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                inter.append(A[i])
                i += 1
                j += 1
            
            elif A[i] < B[j]:
                i += 1
            
            elif A[i] > B[j]:
                j += 1
                
        
        return inter


