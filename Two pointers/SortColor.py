class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        l = len(A)
        zero_count = 0
        one_count = 0
        
        for i in range(l):
            if A[i] == 0:
                zero_count += 1
            elif A[i] == 1:
                one_count += 1
        
        
        return [0]*zero_count + [1] * one_count + [2]*(l-zero_count - one_count)

