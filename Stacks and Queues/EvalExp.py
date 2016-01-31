class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        def calc(a, b, oper):
            if oper == "+":
                return a + b
            elif oper == "-":
                return a - b
            elif oper == "*":
                return a * b
            else:
                if a * b < 0 and a % b != 0:
                    return a / b + 1
                else:
                    return a/b
                
        st = []
        i = 0
        while i < len(A):
            if A[i] in '+-*/':
                b = st.pop()
                a = st.pop()
                st.append(calc(a,b,A[i]))
            else:
                st.append(int(A[i]))
            i += 1
                

        
        return int(st[0])

