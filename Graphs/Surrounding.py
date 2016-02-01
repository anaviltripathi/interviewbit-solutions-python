class Solution:
    # @param A : list of list of chars
    def solve(self, board):
        if not board: return
        m = len(board)
        n = len(board[0])
        
        stack = [ij for k in range(m+n) for ij in ((0,k),(m-1,k),(k,0),(k,n-1))]
        while stack:
            x, y = stack.pop()
            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                stack += [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
                board[x][y] = "S"
        
        board[:] = [["XO"[c=="S"] for c in row] for row in board ]
            

