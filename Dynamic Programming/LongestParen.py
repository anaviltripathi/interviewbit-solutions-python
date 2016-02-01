class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        s = A
        n = len(s)
        longest = [0]*n
        max_length = 0
        
        for i in range(n):
            if s[i]== ")":
                if i - 1 >= 0 and s[i-1] == "(":
                    longest[i] = 2 if i == 1 else longest[i-2] + 2
                    max_length = max(max_length, longest[i])
                else:
                    if i- longest[i-1] -1 >=0 and s[i- longest[i-1] -1] == "(":
                        longest[i] = longest[i-1] + 2 + (longest[i-longest[i-1] - 2] if i-longest[i-1] - 2 >= 0  else 0)
                        max_length = max(max_length, longest[i])
        
        
        return max_length

