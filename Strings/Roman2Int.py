class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        s = []
        num = 0
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        i = 1
        
        while i < len(A)+1:
            #print i
            num += d[A[-i]]
            if i < len(A) and ((A[-i-1] == 'I' and (A[-i] == 'V' or A[-i] == 'X'))
                        or (A[-i-1] == 'X' and (A[-i] == 'L' or A[-i] == 'C'))
                        or (A[-i-1] == 'C' and (A[-i] == 'D' or A[-i] == 'M'))):
                i += 1
                num -= d[A[-i]]
            #print num
            i += 1    
        
        return num
