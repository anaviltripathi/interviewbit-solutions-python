class Solution:
    # @param n : integer
    # @param k : integer
    # @return a strings
    def getPermutation(self, n, k):
        d = {0: 1}
        
        for i in range(1,n+1):
            d[i] = d[i-1]*i
        #print d
        l = range(1,n+1)
        s = ""
        while k:
            i = k/d[len(l)-1]
            #print k/d[len(l)-1], i
            if i == len(l):
                s += str(l[-1])
                k -= (i)*d[len(l)-1]
                l.pop(-1)
            else:
                
                k -= (i)*d[len(l)-1]
                if not k:
                    s += str(l[i-1])
                    l.pop(i-1)
                else:
                    s += str(l[i])
                    l.pop(i)
                
            #print s
        
        if l:
            s += ''.join(map(str,l[::-1]))
        return s

