class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        st = []
        if not A:
            return 0
        for a in A:
            if not st or a != ")":
                st.append(a)
            else:
                encountered_operator = False
                while st and st[-1] != "(":
                    if st[-1] in "+-*/":
                        encountered_operator = True
                    st.pop()
                
                if not encountered_operator:
                        return 1
                if st:
                    st.pop()
                    
        return 0

