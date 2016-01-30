class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A < 2: return A
        root = A
        
        while root * root > A:
            root = (root + A/root)/2
        return root
