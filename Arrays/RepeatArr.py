class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        from collections import defaultdict
        from math import sqrt
        d = defaultdict(int)
        c = set()
        
        for i in A:
            d[int(sqrt(i))] += 1
        
        for i in A:
            if d[int(sqrt(i))] > 1:
                if i not in c:
                    c.add(i)
                else:
                    return i
                    
