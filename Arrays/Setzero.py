class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)
        n = len(A[0])
        row= [1]*m
        col= [1]*n
        for i in range(m):
            for j in range(n):
                if(A[i][j]==0):
                    row[i]=0
                    col[j]=0
                    
        
        for i in range(m):
            if(row[i]==0):
                A[i]= [0]*n
        for j in range(n):
            if(col[j]==0):
                for i in range(m):
                    A[i][j]=0
        return A

