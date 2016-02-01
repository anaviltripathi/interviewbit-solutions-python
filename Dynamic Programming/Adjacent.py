class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        L = [0 for i in range(len(A[0]) + 3)]
        for i in range(len(A[0])):
            L[i+3] = max(L[i+1], L[i]) + max(A[0][i], A[1][i])
        return L[-1] if L[-1] > L[-2] else L[-2]
