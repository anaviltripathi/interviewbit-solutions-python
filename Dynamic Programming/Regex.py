class Solution:
    # @param s : string
    # @param p : string
    # @return an integer
    def isMatch(self, s, p):
        match = 0
        asterisk = -1
        i, j  = 0,0
        m = len(s)
        n = len(p)

        while i < m:
            if j < n and p[j] == "*":
                match = i
                asterisk = j
                j += 1
            elif j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif asterisk >= 0:
                i = match
                match += 1
                j = asterisk + 1
            else:
                return False
        while j < n and p[j] == "*":
            j += 1
        
        return True if j == n else False

