class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        i = 0
        j = 0
        
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                i += 1
            else:
                A.insert(i, B[j])
                j += 1
                i += 1

        
        if j < len(B):
            A += B[j:]
        
        return A

