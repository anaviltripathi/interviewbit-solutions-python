class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        m = len(A)
        n = len(A[0])
        left = [0] * n
        right = [n for i in range(n)]
        height  = [0] * n
        max_area = 0
        
        for i in range(m):
            curr_left = 0
            curr_right = n
            for j in range(n):
                if A[i][j] == 1:
                    left[j] = max(curr_left, left[j])
                    height[j] += 1
                else:
                    left[j] = 0
                    height[j] = 0
                    curr_left = j + 1

                if A[i][-j-1] == 1:
                    right[-j-1] = min(right[-j-1], curr_right)
                else:
                    right[-j-1] = n
                    curr_right = n-j-1
                    
            for j in range(n):
                max_area = max(max_area, (right[j] - left[j]) * height[j])
                
        return max_area
        
        

