class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, beginWord, endWord, dictV):
        if beginWord == endWord:
            return [[beginWord]]
        wordlist = set(dictV)
        wordLength = len(beginWord)
        fronts = [{beginWord}, {endWord}]
        ans = []
        parents = {beginWord: None, endWord: None}
        wordlist.discard(beginWord)
        wordlist.discard(endWord)
        import string
        while fronts[0] and fronts[1] and not ans:
            if len(fronts[0]) > len(fronts[1]):
                fronts.reverse()
        
            newLevel = set()
            for word in fronts[0]:
                for i in range(wordLength):
                    for c in string.lowercase:
                        if c == word:
                            continue
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in fronts[1]:
                            self.buildLadders(word, newWord, beginWord, endWord, parents, ans)
                        if newWord in newLevel:
                            parents[newWord].append(word)
                        if newWord in wordlist:
                            newLevel.add(newWord)
                            wordlist.remove(newWord)
                            parents[newWord] = [word]
                            
            fronts[0] = newLevel
        
        return ans
    
    def buildLadders(self, aword, bword, beginWord, endWord, parents, ans):
        paths = [[],[]]
        path1 = [aword]
        self._build(path1, parents, paths[0])
        path2 = [bword]
        self._build(path2, parents, paths[1])
        
        if paths[0][0][-1] != beginWord:
            paths.reverse()
        
        for path in paths[0]:
            path.reverse()
            
        
        for prefix in paths[0]:
            for suffix in paths[1]:
                ans.append(prefix + suffix)
        
    def _build(self,path, parents, paths):
        #print path
        if not parents[path[-1]]:
            paths.append(path[:])
        else:
            for nextWord in parents[path[-1]]:
                path.append(nextWord)
                self._build(path, parents, paths)
                path.pop()
                
    
