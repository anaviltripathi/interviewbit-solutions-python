class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, A, B):
        if not A: return 0
        change = [0] * (B+1)
        change[0] = 1
        for i in range(len(A)):
            for j in range(A[i], B+1):
                change[j] += change[j - A[i]]
                change[j] %= 1000007
        return change[-1]

