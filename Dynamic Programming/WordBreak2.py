class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, s, wordDict):
        return findWords(0, len(s), s, wordDict, {})


def findWords(start, end, s, wordDict, cache):
    if start in cache:
        return cache[start]
    
    cache[start] = []
    current = start
    candidate = ''
    
    while current < end:
        candidate += s[current]
        current += 1
        if candidate in wordDict:
            if current == end:
                cache[start].append(candidate)
            else:
                for x in findWords(current, end, s, wordDict, cache):
                    cache[start].append(candidate + ' ' + x)
    
    return cache[start]
        

