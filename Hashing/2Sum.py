class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, nums, target):
        d = {}
        
        for i in range(len(nums)):
            if nums[i] not in d:
                if target - nums[i] not in d:
                    d[nums[i]] = i + 1
                else:
                    return [d[target - nums[i]] , i + 1]
            else:
                if target - nums[i] in d:
                    return [d[target - nums[i]] , i + 1]
                    
        return []
