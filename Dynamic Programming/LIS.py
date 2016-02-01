class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        if not A: return 0
        n = len(A)
        l = [1] * n
        for i in range(1, n):
            for j in range(0,i):
                if A[i] > A[j] and l[i] < l[j] + 1:
                    l[i] = l[j] + 1
        return max(l)

