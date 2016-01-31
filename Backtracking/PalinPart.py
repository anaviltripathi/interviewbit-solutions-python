class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, s):
        return [[s[:i]] + rest for i in range(1,len(s)+1) if s[:i] == s[:i][::-1] for rest in self.partition(s[i:]) or [[]]]    

