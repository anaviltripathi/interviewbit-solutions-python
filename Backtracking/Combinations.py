class Solution:
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers
    def combine(self, n, k):
        return self.comb_helper(1,n+1,k)
    
    def comb_helper(self,start, end, k):
        #print start, end , k
        if end - start  == k:
            #print start, end , k
            return [range(start, start + k)]
        elif k == 0:
            return [[]]
            #return [range(start, end+1)]
            
        all_combs = []
        
        for i in range(start, end+1 - k):
            for comb in self.comb_helper(i + 1, end, k - 1):
                all_combs.append([i]+comb)
        
        return all_combs

