class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        beginWord = start
        endWord = end
        wordList = dictV
        import string
        
        if beginWord == endWord: return 1
        wordLength = len(beginWord)
        fronts = [{beginWord}, {endWord}]
        levels = [1,1]

        while fronts[0] and fronts[1]:
            if len(fronts[0]) > len(fronts[1]):
                fronts.reverse()
                levels.reverse()
            newLevel = set()
            for word in fronts[0]:
                for i in range(wordLength):
                    for c in string.lowercase:
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in fronts[1]:
                            return levels[0] + levels[1]
                        if newWord in wordList:
                            newLevel.add(newWord)
                            wordList.remove(newWord)


            fronts[0] = newLevel
            levels[0] += 1

        return 0

