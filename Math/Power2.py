class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A < 2:
            return True
            
        import math
        for x in range(2, int(math.sqrt(A))+ 1):
            y = 2
            p = pow(x, y)
            while p <= A:
                if p == A:
                    return True
                y += 1
                p = pow(x,y)
        
        return False
