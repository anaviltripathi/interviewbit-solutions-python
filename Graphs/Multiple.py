class Solution:
    # @param A : integer
    # @return a strings
    def multiple(self, A):
        #num = str(A)
        #level = ['0']*len(num)
        #level[0] = '1'
        #level = [int(''.join(level))]
        level = [1]
        seen = [0]*A
        par = [0]*A
        val = [0]*A
        from collections import deque
        qu = deque()
        qu.append(1%A)
        seen[1%A] = 1
        val[1%A] = 1
        
        
        res = ""
        while True:
            p = qu.popleft()
            if p == 0:
                #print "oK"
                res = "1" if val[p] == 1 else '0'
                p = par[p]
                while p != 0:
                    res = "1" + res if val[p] == 1 else '0' + res
                    p = par[p]
                return res
            
            q = (p*10)%A
            if seen[q] == 0:
                qu.append(q)
                seen[q], par[q], val[q] = 1, p, 0
            
            q += 1
            if q >= A: q -= A
            
            if seen[q] == 0:
                qu.append(q)
                seen[q], par[q], val[q] = 1, p, 1
                
                

