class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        
        if A < 0:
            return -int(str(-A)[::-1]) if -int(str(-A)[::-1]) > -2147483647 else 0
            
        else:
            return int(str(A)[::-1]) if int(str(A)[::-1]) < 2147483647 else 0

