class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        if len(A) == 0: return []
        max_sub = []
        curr_sub = []
        curr_sum = 0
        max_sum = -1
        
        for i in range(len(A)):
            if A[i] >=0 :
                curr_sub.append(A[i])
                curr_sum += A[i]
            else:
                curr_sum = 0
                curr_sub = []
            if curr_sum > max_sum:
                max_sub = curr_sub
                max_sum = curr_sum
            elif curr_sum == max_sum and len(max_sub) <= len(curr_sub):
                max_sub = curr_sub
                max_sum = curr_sum
                
        return max_sub

