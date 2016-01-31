class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        board = ["."*A for i in range(A)]
        return self.queensHelper(board)
        
    def queensHelper(self, board):
        list_of_boards = []
        board_length = len(board)
        row = 0
        while row < board_length and 'Q' in board[row]:
            row += 1
        
        if row == board_length: 
            return [board]
        
        for col in range(board_length):
            board[row] = ['.']*board_length
            board[row][col] = 'Q'
            board[row] = ''.join(board[row])
            
            if self.constraintCheck(board, row, col):
                for final_board in self.queensHelper(board):
                    list_of_boards.append(final_board)
                board = board[:row] + ["."*board_length]* (board_length- row)
            else:
                board = board[:row] + ["."*board_length]* (board_length- row)
                pass

        return list_of_boards
                
                
        
    def constraintCheck(self, board, row, col):
        for i in range(len(board)):
            for j in range(len(board)):
                if i != row or j != col:
                    if board[i][j]== 'Q' and (abs(i - row) == abs(j - col)) :
                        return False
                    if board[i][j] == 'Q' and  j == col:
                        return False
                    if board[i][j] == 'Q' and  i == row:
                        return False
        
        return True
        
