class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        num1 = A
        num2 = B
        
        res = [0]* (len(num1) + len(num2))
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                res[i+j] += int(e1) * int(e2)
                res[i+j+1] += res[i+j]/10
                res[i+j] %= 10

        while len(res) > 1 and res[-1] == 0: res.pop()
        
        return ''.join( map(str,res[::-1]) )

