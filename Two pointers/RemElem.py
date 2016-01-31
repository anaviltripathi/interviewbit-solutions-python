class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        n = len(A)
        
        count = 0
        
        for i in range(n):
            if A[i] == B:
                continue
            else:
                A[count] = A[i]
                count += 1
        
        #A[:] = filter(lambda x: x != B, A) 
        
        return count
        

