class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if haystack is None or needle is None: return -1
        h = self.preprocess(needle)
        
        i = 0
        j = 0
        while i < len(haystack):
            if needle[j] == haystack[i]:
                j += 1
                i += 1
            if j == len(needle): return i - j
            elif i < len(haystack) and needle[j] != haystack[i]:
                if j!=0:
                    j = h[j-1]
                else:
                    i += 1
        return -1 
        
    def preprocess(self, pattern):
        lps = [0]
        matching_prefix_position = 0
        for i in range(1,len(pattern)):
            while matching_prefix_position != 0 and pattern[i] != pattern[matching_prefix_position]:
                matching_prefix_position = lps[matching_prefix_position-1]
            if pattern[matching_prefix_position] == pattern[i]:
                matching_prefix_position += 1
            lps.append(matching_prefix_position)

        return lps
        

