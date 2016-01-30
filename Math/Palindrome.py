class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        def reverse(n):
            res = 0
            while n:
                temp = n % 10
                res = res*10 + temp
                n /= 10
            
            return res
        
        if A < 0:
            return False
        
        return A == reverse(A)

