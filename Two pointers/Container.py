class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        if len(A) < 2: return 0
        i = 0
        area = 0
        maxContainer = 0
        while i < len(A) - 1:
            j = len(A) - 1
            area = 0
            while i < j:
                if A[j] < A[i]:
                    area = max(area, (j-i)*A[j])
                    j -= 1
                else:
                    area = max(area, (j-i) * A[i])
                    break
                
            maxContainer = max(maxContainer, area)
            i += 1
                    
        
        return maxContainer

