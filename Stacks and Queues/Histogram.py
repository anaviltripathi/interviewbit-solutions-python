class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, height):
        st = []
        maxArea = 0
        i = 0
        for i in range(len(height)):
            if not st or height[st[-1]] <= height[i]:
                st.append(i)
            else:
                #maxArea = max(maxArea, height[i])

                while st and height[st[-1]] > height[i]:
                    tp = st.pop()
                    if st:
                        maxArea = max(maxArea, height[tp] * ( i - st[-1] - 1))
                    else:
                        maxArea = max(maxArea, height[tp] * i)
                        #print maxArea, st
                 
                st.append(i)
                
        i += 1
        while st:
            tp = st.pop()
            if st:
                maxArea = max(maxArea, height[tp] * ( i - st[-1] - 1))
            else:
                maxArea = max(maxArea, height[tp] * i)
            #print maxArea, st, i
        
        return maxArea

