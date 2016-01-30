class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) < 2:
            return 0
        nums = A
        length = len(A)
        if length == 2: return abs(nums[0]- nums[1])
        else:
            min_nums = min(nums)
            max_nums = max(nums)
            diff = max_nums - min_nums
            if diff == 0: return 0
            bucket = [[sys.maxint, -sys.maxint -1] for i in range(length-1)]
                
            for i in range(length):
                if bucket[int((length-2)*(nums[i]-min_nums)/diff)][0] > nums[i]:
                    bucket[int((length-2)*(nums[i]-min_nums)/diff)][0] = nums[i]
                if bucket[int((length-2)*(nums[i]-min_nums)/diff)][1] < nums[i]:
                    bucket[int((length-2)*(nums[i]-min_nums)/diff)][1] = nums[i]
            
            #print bucket
            
            max_diff = bucket[0][1] - bucket[0][0]
            prev_max = bucket[0][1]
            for i in range(1,length-1):
                if bucket[i][0] != sys.maxint:
                    current_min = bucket[i][0]
                    max_diff = max(max_diff, current_min-prev_max)
                    max_diff = max(max_diff, bucket[i][1] - bucket[i][0])
                    prev_max = bucket[i][1]
                    #print bucket[i]
                
            return max_diff
            
