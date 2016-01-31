class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        if len(A) == 0: return None
        max_pal = ""
        for i in xrange(len(A)):
            p1 = self.expandAroundCenter(i,i, A)
            if len(p1) > len(max_pal):
                max_pal = p1
            p2 = self.expandAroundCenter(i, i+1, A)
            if len(p2) > len(max_pal):
                max_pal = p2
                
        return max_pal
    
    def expandAroundCenter(self, left,right, A):
        while(left >=0 and right < len(A) and A[left] == A[right]):
            left -= 1
            right +=1 
        return A[left+1: right]
                        
                        
        
        
