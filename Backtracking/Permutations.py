class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if len(A) == 1: return [A]
        permus = []
        for i in range(len(A)):
            for l in self.permute(A[:i] + A[i+1:]):
                permus.append([A[i]] + l)
                
        
        return permus
            

