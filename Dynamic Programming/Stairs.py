class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        stairs = [1]*(A+1)
        for i in range(2,len(stairs)):
            stairs[i] = stairs[i-1] + stairs[i-2]
        return stairs[-1]
