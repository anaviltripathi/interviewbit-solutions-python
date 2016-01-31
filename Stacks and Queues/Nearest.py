class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        if not arr : return None
        st = []
        res = []
        for a in arr:
            while st and st[-1] >= a:
                st.pop()
            if not st:
                res.append(-1)
            else:
                res.append(st[-1])
            st.append(a)
        
        return res

