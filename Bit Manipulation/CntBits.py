class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        if len(A) <= 1: return 0
        
        s = 0
        m = len(A)
        k = 0
        while k < 31:
            n = 0
            for i in range(m):
                if A[i] & 1:
                    n += 1
                A[i] >>= 1
            s += 2*abs((m - n) * n)
            s %= (pow(10,9) + 7)
            k += 1
            
        return s

