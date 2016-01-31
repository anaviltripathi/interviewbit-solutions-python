class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        if not A: return 0
        j = 0
        while j < len(A) and A[~j] == ' ':
            j += 1
        
        i = j
        length = 0
        while i < len(A):
            if A[~i] == " ":
                return length
            length += 1
            i += 1
            
        return length
