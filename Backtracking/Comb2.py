class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, candidates, target):
        sorted_list = sorted(candidates)
        all_combinations = self.combinationHelper(sorted_list, 0, target)
        return all_combinations
    
    
    def combinationHelper(self, candidates, start, target):
        if target == 0:
            return [[]]
        result = []
        
        for i in range(start, len(candidates)):
            if i != start and candidates[i] == candidates[i-1]:
                continue
            elif candidates[i] > target: 
                break
            else:
                for r in self.combinationHelper(candidates, i+1, target - candidates[i]):
                    result.append([candidates[i]]+ r)
        
        return result

