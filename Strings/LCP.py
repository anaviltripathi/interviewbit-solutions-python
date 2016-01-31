class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        res = ""
        min_length = min(map(len,A))
        #print min_length
        
        for i in range(min_length):
            curr = ""
            for s in A:
                if curr and curr != s[i]:
                    return res
                else:
                    curr = s[i]
            res += curr
            
        return res

