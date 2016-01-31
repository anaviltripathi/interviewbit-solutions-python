class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        p = len(A)
        q = len(B)
        r = len(C)
        import sys
        res = sys.maxint
        i, j, k = 0,0 ,0 
        while i < p and j < q and k < r:
            min_e, max_e = min(A[i],B[j],C[k]), max(A[i],B[j],C[k])
            if res > max_e - min_e:
                res = max_e - min_e
                if res == 0:
                    return 0
            if A[i] == min_e:
                i += 1
            elif B[j] == min_e:
                j += 1
            else:
                k += 1
        
        return res

