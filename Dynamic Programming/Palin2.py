class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        breaks = [i for i in range(-1,len(A))]
        
        for i in range(len(A)):
            r1 , r2 = 0, 0
            
            #odd length
            while i -r1 >= 0 and i + r1 < len(A) and A[i-r1] == A[i + r1]:
                breaks[i + r1 + 1] = min(breaks[i + r1 + 1], breaks[i-r1] + 1)
                r1 += 1
            
            #even length
            while i - r2 > 0 and i + r2 < len(A) and A[i -r2 -1] == A[i + r2]:
                breaks[i + r2 + 1] = min(breaks[i + r2 + 1], breaks[i-r2-1] + 1)
                r2 += 1
            
        return breaks[-1]

