class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        nums = A
        k = B
        if not nums:
            return nums
        st = []
        for i in range(k):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            st.append(i)
        
        l = [nums[st[0]]]
        
        n = len(nums)
        for i in range(k,n):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            while st and i - st[0] >= k:
                st.pop(0)
            st.append(i)
            l.append(nums[st[0]])
            
        return l

