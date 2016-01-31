class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        s = 0
        while A != 0:
            s += A % 2
            A /= 2
        return s

