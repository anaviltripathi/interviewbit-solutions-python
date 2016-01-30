class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        n = len(A)
        for i in range(0,n,2):
            if i + 1 < n:
                A[i], A[i+1] = A[i+1], A[i]
                
        return A
                

