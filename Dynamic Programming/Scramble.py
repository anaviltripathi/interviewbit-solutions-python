class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isScramble(self, A, B):
        s1, s2 = A, B
        if s1 == s2:
            return True
        if not s1 or not s2:
            return False
        if len(s1) != len(s2):
            return False
        from collections import defaultdict
        lcount1 = defaultdict(int)
        lcount2 = defaultdict(int)
        rcount2 = defaultdict(int)
        n = len(s1)
        for i in range(n-1):
            lcount1[s1[i]] += 1
            lcount2[s2[i]] += 1
            rcount2[s2[n-i-1]] += 1
            if lcount1 == lcount2:
                if self.isScramble(s1[:i+1], s2[:i+1]) and self.isScramble(s1[i+1:], s2[i+1:]):
                    return True
            elif rcount2 == lcount1:
            
                if self.isScramble(s1[:i+1], s2[n-i-1:]) and self.isScramble(s1[i+1:], s2[:n-i-1]):
                    return True
        return False

