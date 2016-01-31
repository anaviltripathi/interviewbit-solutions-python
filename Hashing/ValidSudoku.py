class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        rowD = [{} for i in range(9)]
        colD = [{} for i in range(9)]
        boxD = [{} for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                ele = A[i][j]
                if ele != '.':
                    if A[i][j] not in rowD[i]:
                        rowD[i][A[i][j]] = 1
                    else:
                        return 0
                    if A[i][j] not in colD[j]:
                        colD[j][A[i][j]] = 1
                    else:
                        return 0
                    boxNumber = 3 * (i/3) + (j/3)
                    if ele not in boxD[boxNumber]:
                        boxD[boxNumber][ele] = 1
                    else:
                        return 0
            
        return 1

