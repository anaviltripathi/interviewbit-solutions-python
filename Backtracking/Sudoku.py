class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        board = A
        flag = False
        
        for i in range(9):
            for j in range(9):
                tried_all_value = 9
                if board[i][j] == '.':
                    for val in map(str,range(1,10)):
                        if self.checkConstraint(board,val, i ,j):
                            board[i][j] = val
                            self.solveSudoku(board)
                            if board:
                                flag = True
                                for row in board:
                                    if '.' in row:
                                        flag = False
                                        break
                        if flag: break
                        else:
                            board[i][j] = '.'
                        tried_all_value -= 1
                if tried_all_value ==0:
                    return

                if flag:break
            
            if tried_all_value == 0:
                break
            if flag: break
        
                            
    def checkConstraint(self, board, val,i,j):
        if val in board[i]:
            return False

        for row in board:
            if row[j] == val:
                return False
    
        for m in range(3):
            for n in range(3):
                if board[(i//3)*3 + m][(j//3)*3 + n] == val:
                    return False
    
        return True

