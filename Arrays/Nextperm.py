class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        is_sorted = True
        if len(A) <= 1: return A
        smallest = -1
        for i in range(len(A)-1, 0, -1):
            if A[i] > A[i-1]:
                j = i
                while j < len(A) and A[i-1] < A[j]:
                    j += 1
                
                A[i-1], A[j-1] = A[j-1], A[i-1]
                
                A[i:] = sorted(A[i:])
                is_sorted = False
                break
            else: 
                smallest = i
            
        
        return sorted(A) if is_sorted == True else A

