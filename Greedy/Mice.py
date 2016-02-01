class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A = sorted(A)
        #print A
        B = sorted(B)
        #print B
        import sys
        
        maxdiff = -sys.maxint - 1
        
        for i in range(len(A)):
            maxdiff = max( maxdiff, abs(A[i] -B[i]) )
                
        return maxdiff
                    

