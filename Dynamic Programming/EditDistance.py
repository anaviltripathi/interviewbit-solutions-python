class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        edit = [[0]* (len(B) + 1) for i in range(len(A) + 1)]
        for i in range(len(A)+1):
            for j in range(len(B)+1):
                if i == 0:
                    edit[i][j] = j
                elif j == 0:
                    edit[i][j] = i
                elif A[i-1] == B[j-1]:
                    edit[i][j] = edit[i-1][j-1]
                else:
                    edit[i][j] = 1 + min(edit[i-1][j-1], edit[i-1][j] , edit[i][j-1])
        return edit[-1][-1]

