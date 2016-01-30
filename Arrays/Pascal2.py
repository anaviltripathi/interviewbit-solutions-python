class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A == 0:  return [1]
        pascal = [[0] * (A+1) for i in range(2)]
        pascal[0][0] = 1
        
        for i in range(1,A+1):
            for j in range(i+1):
                if j == 0:
                    pascal[1][j] = 1
                else:
                    pascal[1][j] = pascal[0][j-1] + pascal[0][j]
                    
            pascal[0] = pascal[1][:]
        
        return pascal[1]

