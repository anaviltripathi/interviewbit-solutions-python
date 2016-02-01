class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        if len(A) == 1: return 1
        i = len(A) - 1
        while i >= 0:
            reachable = False
            dist = 1
            j = i - 1
            while j >= 0 and not reachable:
                if A[j] >= dist:
                    reachable = True
                else:
                    j -= 1
                    dist += 1
            if i == 0: return 1
            if not reachable: return 0
            else:
                i = j
        return 0
