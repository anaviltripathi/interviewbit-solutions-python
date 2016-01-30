class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        val = 5
        res = 0
        i = 1
        while A >= val**i:
            res += A/(val**i)
            i += 1
        
        return res

