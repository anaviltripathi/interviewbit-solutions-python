class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        res = ""
        while A > 0:
            A -= 1
            temp = A%26
            A /= 26
            res += chr(ord('A')+temp)
                    
        return res[::-1]

