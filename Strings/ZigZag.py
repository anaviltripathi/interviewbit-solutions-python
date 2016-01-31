class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        s = ""
        if B == 1: return A
        for i in range(B):
            step_size = 2*(B-1)
            j = i
            nex = 2 * i
            while j < len(A):
                s += A[j]
                nex = abs(step_size - nex)
                if nex !=0 : 
                    j += nex
                else: 
                    nex = abs(step_size - nex)
                    j += nex
        return s
