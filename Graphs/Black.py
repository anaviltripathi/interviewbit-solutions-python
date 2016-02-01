class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, grid):
        if not grid:
            return 0
        visited = [[False]*len(grid[0]) for _ in xrange(len(grid))]
        def sink(i,j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 'X' and not visited[i][j]:
                visited[i][j] = True
                map(sink, (i-1, i+1, i, i), (j, j, j - 1, j+1))
                return 1
            return 0
        
        return sum(sink(i,j) for i in range(len(grid)) for j in range(len(grid[i])))

