class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        s = sorted(list(A))
        f = 1
        rank = 1
        length = len(A)
        
        for i in range(len(A)):
            length -= 1
            n = s.index(A[i])
            s.remove(A[i])
            f = 1
            for j in range(length):
                f *= (j + 1)
            rank += (n * (f)) % 1000003

        return rank % 1000003
        
