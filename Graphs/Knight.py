class Solution:
    # @param N : integer
    # @param M : integer
    # @param x1 : integer
    # @param y1 : integer
    # @param x2 : integer
    # @param y2 : integer
    # @return an integer
    def knight(self, N, M, x1, y1, x2, y2):
        visited = [[False]*M for i in range(N)]
        queue = [((x1,y1),0)]
        visited[x1-1][y1-1] = True
        def append_paths(i,j, depth):
            for x, y in ((1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)):
                if 1 <= i + x <= N and 1 <= j + y <= M and not visited[x+i-1][y+j-1]:
                    queue.append(((x+i,y+j),depth+1))
                    visited[x+i-1][y+j-1] = True
        
        while queue:
            (i,j), d = queue.pop(0)
            if i == x2 and j == y2:
                return d
            else:
                append_paths(i,j,d)
        
        return -1

