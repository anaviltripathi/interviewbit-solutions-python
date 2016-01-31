class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        s = []
        
        for c in A:
            if 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9':
                s.append(c)
        
        s = ''.join(s)
        
        #print s.lower(), s[::-1].lower()
        if s.lower() == s[::-1].lower():
            return True
        else:
            return False

