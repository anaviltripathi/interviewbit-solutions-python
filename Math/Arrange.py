class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        N = len(A)
        for i in range(len(A)):
            A[i] = A[i] + A[A[i]%N]%N * N
        
        for i in range(len(A)):
            A[i] /= N
        
        
