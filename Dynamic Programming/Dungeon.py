class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        dungeon = A
        m = len(dungeon)
        n = len(dungeon[0])
        #dp = [[0]*(n) for i in range(m)]
        dungeon[-1][-1] = 1 if dungeon[-1][-1] >= 0 else -dungeon[-1][-1] + 1

        
        for j in range(1,n):
            dungeon[-1][-j-1] = max(dungeon[-1][-j] - dungeon[-1][-j-1], 1)
            
        for i in range(1,m):
            dungeon[-i-1][-1] = max(dungeon[-i][-1] - dungeon[-i-1][-1], 1)
            
        for i in range(1,m):
            for j in range(1,n):
                dungeon[-i-1][-j-1] = max(1, min(dungeon[-i-1][-j], dungeon[-i][-j-1]) - dungeon[-i-1][-j-1])
        
        return dungeon[0][0]

