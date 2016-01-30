class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        B = []
        for i in range(len(A)):
            if A[i] == '\n': continue
            s += int(A[i])
            if A[i] == '1':
                B.append(-1)
            else:
                B.append(1)
                
        max_here = 0
        max_so_far = 0
        c_start = 1 
        end = -1
        for i, x in enumerate(B):
            #print i
            if max_here+x < 0 :
                c_start = i + 2
                max_here = 0
            else:
                max_here += x
                
                
            if max_here > max_so_far:
                start = c_start
                end = i + 1
                max_so_far = max_here
        
        if end == -1:
            return []
        else:
            return [start, end]

            
        
