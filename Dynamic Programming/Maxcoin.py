class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, nums):
        
        '''
        if not nums:
            return 0
        n = len(nums)
        dp = [[0]*n for i in range(n)]
        for gap in range(n):
            for i in range(n-gap):
                if gap == 0:
                    dp[i][i] = nums[i]
                elif gap == 1:
                    dp[i][i+1] = max(nums[i],nums[i+1])
                else:
                    dp[i][i+gap] = max(nums[i] + min(dp[i+2][i+gap],dp[i+1][i+gap-1]), nums[i+gap] + min(dp[i+1][i+gap-1] , dp[i][i+gap-2]))

        return dp[0][-1]
        '''
        cache = {}
        def helper(nums):
            if len(nums) == 2:
                return max(nums)
            
            if tuple(nums) in cache:
                return cache[tuple(nums)]
            
            choice1 = nums[0] + min(helper(nums[1:-1]), helper(nums[2:]))
            choice2 = nums[-1] + min(helper(nums[1:-1]), helper(nums[:-2]))
            cache[tuple(nums)] = max(choice1, choice2)
            return cache[tuple(nums)]
            
        return helper(nums)

