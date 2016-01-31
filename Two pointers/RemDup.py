class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        count = 0
        i = 0
        while i < len(A):
            if i == 0 or A[i] != A[i-1]:
                A[count] = A[i]
                count += 1
            
            i += 1
            
        return count

