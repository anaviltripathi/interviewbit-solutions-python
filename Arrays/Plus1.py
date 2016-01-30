class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        res = []
        added = False
        
        while A and not A[0]:
            A = A[1:]
        
        if not A: return [1]
        
        for i in range(1,len(A)+1):
            if A[-i] == 9 and not added:
                res.append(0)
                if i == len(A):
                    res.append(1)
                    added = True
            elif A[-i] != 9 and not added:
                res.append(A[-i]+ 1)
                added = True
            else:
                res.append(A[-i])
                
                
        return res[::-1]
            

