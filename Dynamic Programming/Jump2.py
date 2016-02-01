class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        nums = A
        i = 0
        jumps = 0
        last_max_reachable_index = 0
        current_max_reachable_index = 0
        while last_max_reachable_index < len(nums)-1:
            while i <= last_max_reachable_index:
                current_max_reachable_index = max(i + nums[i], current_max_reachable_index)
                i += 1
            if last_max_reachable_index == current_max_reachable_index: return -1
            last_max_reachable_index = current_max_reachable_index
            jumps += 1
        return jumps
