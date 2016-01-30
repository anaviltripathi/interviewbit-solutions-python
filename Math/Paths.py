class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        if A== 1 or B== 1: return 1
        
        fact_A = 1
        fact_B = 1
        fact_A_B = 1
        for i in range(1,A+B-1):
            fact_A_B *= i
            if i < B:
                fact_B *= i
            if i < A:
                fact_A *= i
        
        return fact_A_B/(fact_B*fact_A)

