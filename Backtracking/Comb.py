class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A = set(A)
        A = list(A)
        A = sorted(A)
        comb_lis = self.combinationHelper(A, 0, B)
        return comb_lis[0]
        
        
        
    def combinationHelper(self, A, value, target):
        comb_lis = []
        found = False
        if value == target:
            return comb_lis, True
        else:
            i = 0
            while i < len(A) and A[i] + value <= target:
                lis_of_lis, found = self.combinationHelper(A[i:], value + A[i], target)
                if lis_of_lis == [] and found == True:
                    comb_lis.append([A[i]])
                else:
                    for lis in lis_of_lis:
                        comb_lis.append( [A[i]] + lis )
                        
                i += 1
            
            return comb_lis, found
                

