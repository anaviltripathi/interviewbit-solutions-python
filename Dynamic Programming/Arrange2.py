class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def arrange(self, A, B):
        if len(A.strip()) < B:
            return -1
        
        from sys import maxint
        def arrange_util(h, n):
            if n == 1:
                #print h
                white = 0
                black = 0
                for c in h:
                    if c == "W":
                        white += 1
                    else:
                        black += 1
                
                cache[(B-n, len(h))] =  white * black
                return cache[(B-n, len(h))]
            else:
                if (B-n, len(h)) not in cache:
                    num_of_horses = len(h)
                    max_poss = num_of_horses - n + 1
                    #print "max_poss: ", max_poss
                    black = 0
                    white = 0
                    cache[(B-n, len(h))] = maxint
                    
                    for i in range(max_poss):
                        if h[i] == "W":
                            white += 1
                        else:
                            black += 1
                        cache[(B-n, len(h))] = min(white*black + arrange_util(h[i+1:], n - 1), cache[(B-n, len(h))])
                    
                return cache[(B-n, len(h))]
                
        cache = {}            
        res = arrange_util(A.strip(), B)
        #print cache
        return res

