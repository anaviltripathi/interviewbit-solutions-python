class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        curr = 0
        p = 0
        
        while curr < len(A):
            if 0 < A[curr] <= len(A):
                pos = A[curr] - 1
                while 0 <= pos < len(A) and A[pos] != pos + 1:
                    k = pos
                    pos = A[pos] - 1
                    A[k] = k + 1
            curr += 1
     
        for i in range(len(A)):
            if A[i] != i + 1:
                return i + 1
                
        return len(A) + 1
        
