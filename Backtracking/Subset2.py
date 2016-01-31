class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, nums):
        if not nums:
            return [[]]
        return sorted(self.subsetHelper(sorted(nums)))
        
    def subsetHelper(self, nums):
        if not nums:
            return []
    
        res = []
        i = 0
        while i < len(nums) and nums[i] == nums[0]:
            i += 1
        
        for subset in self.subsetHelper(nums[i:]) or [[]]:
            for j in range(i+1):
                res += [[nums[0]]*(j) + subset]
        #res += self.subsetHelper(nums[i:])
        return res
        
