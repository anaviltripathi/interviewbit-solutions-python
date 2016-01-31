class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        
        s= A.strip()
        
        state = 1
        for i in range(len(s)):
            if state == 1:
                if s[i] == '+' or s[i] == '-': state = 2
                elif s[i] == '.': state = 4
                elif s[i] <='9' and s[i] >='0': state = 3
                else: return False
            elif state == 2:
                if s[i] <='9' and s[i] >='0': state = 3
                elif s[i] == '.': state = 4
                else: return False
            elif state == 3:
                if s[i] <='9' and s[i] >='0': state = 3
                elif s[i] == '.': state = 4
                elif s[i] == 'e': state = 6
                else: return False
            elif state == 4:
                if s[i] <='9' and s[i] >='0': state = 5
                else: return False 
            elif state == 5:
                if s[i] <='9' and s[i] >='0': state = 5
                elif s[i] == 'e': state = 6
                else: return False 
            elif state == 6:
                if s[i] <='9' and s[i] >='0': state = 8
                elif s[i] == '+' or s[i] == '-': state = 7
                else: return False 
            elif state == 7:
                if s[i] <='9' and s[i] >='0': state = 8
                else: return False 
            elif state == 8:
                if s[i] <='9' and s[i] >='0': state = 8
                else: return False
                
        if state == 3 or (state == 5 and A[-1] != '.') or state == 8: return True
        else: return False

