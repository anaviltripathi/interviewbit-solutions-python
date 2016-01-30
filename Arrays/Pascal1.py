class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A == 0: return []
        
        pascal = [[1] for i in range(A)]
        
        for i in range(1,A):
            prev_row = pascal[i-1]
            for j in range(1,len(prev_row)+1):
                ele = pascal[i-1][j] + pascal[i-1][j-1] if j > 0 and j <len(prev_row) else 1
                pascal[i].append(ele)
            
        
        return pascal

