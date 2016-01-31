class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        d= {0:-1}
        s = 0
        l = -1
        r = -1
        for i,n in enumerate(A):
            s += n
            if s in d:
                if i - d[s] > r - l - 1:
                    l = d[s]
                    r = i+1
            else:
                d[s] = i
                
        if r == -1: 
            return []
            
        return A[l+1:r]
                    
        

