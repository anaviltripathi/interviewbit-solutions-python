class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        return reduce(lambda x,y : x^y, A)

