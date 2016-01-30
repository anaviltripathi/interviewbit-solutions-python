class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        if not K: return False
        arrive = zip(arrive, [1]*len(arrive))
        depart = zip(depart, [-1]*len(arrive))
        s = sorted(arrive + depart)
        
        if len(arrive) < 2:
            if K >= 1:
                return True
            else:
                return False
                
        i = 0
        overlaps = 0
        while i < len(s):
            overlaps += s[i][1]
            if overlaps > K:
                return False
            i += 1
        return True

