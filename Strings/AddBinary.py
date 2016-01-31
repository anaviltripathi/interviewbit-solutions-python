class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        a = A
        b = B
        result = []
        carry = 0
        if len(a) < len(b):
            a , b = b, a
        i = 1
        
        while i <= len(b):
            res = int(a[-i]) + int(b[-i]) + carry
            if res > 1: 
                if res == 2: 
                    res = 0
                else:
                    res = 1
                carry = 1
            else:
                carry = 0
            
            result.append(str(res))
            i +=1 
            
        while i <= len(a):
            res = int(a[-i]) + carry
            if res > 1: 
                if res == 2: 
                    res = 0
                else:
                    res = 1
                carry = 1
            else:
                carry = 0
            i += 1
            
            result.append(str(res))
            
        if carry : result.append(str(carry))
        
        result = result[::-1]
        
        return ''.join(result)
        
