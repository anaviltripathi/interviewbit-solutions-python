class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        s = str(A)
        d = set()
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                x = reduce(lambda x,y : x*y, map(int, s[i:j])) 
                if x in d:
                    return False
                else:
                    d.add(x)
                    
        return True
                    

