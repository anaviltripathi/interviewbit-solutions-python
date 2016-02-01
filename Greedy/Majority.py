class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        if len(A) == 1: return A[0]
        count = 1
        majority_index = 0
        for i in range(1,len(A)):
            if A[majority_index] != A[i]:
                count -= 1
                if count < 1:
                    majority_index = i
                    count = 1
            else:
                count += 1
        return A[majority_index]

