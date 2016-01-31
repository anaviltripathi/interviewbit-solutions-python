class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, height):
        i = 0 
        j = len(height) - 1
        
        maxleft, maxright = 0, 0
        water = 0
        left = 0
        right = len(height) - 1
        
        while left <= right:
            if height[left] <= height[right]:
                if maxleft < height[left]:
                    maxleft = height[left]
                else:
                    water += maxleft - height[left]
                    left += 1
            else:
                if maxright < height[right]:
                    maxright = height[right]
                else:
                    water += maxright - height[right]
                    right -= 1
                    
                    
        return water

