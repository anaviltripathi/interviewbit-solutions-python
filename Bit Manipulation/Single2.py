class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        for n in A:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
        
        return ones
