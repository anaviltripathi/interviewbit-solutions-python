class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        a = 0
        for i in range(32):
            a <<= 1
            a |= A & 1
            A >>= 1
            
        return a

