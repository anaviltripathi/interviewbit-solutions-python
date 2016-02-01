class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, board, word):
        #if len(word) >= 900:
        #    return True
        word = word[:-1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.existhelper(board, word[1:], i, j) == 1:
                        return 1

        return 0

    def existhelper(self, board, word, i, j):
        #if word[0] == "C": print i,j
        if len(word) == 0:
            return 1
        else:
            if j > 0 and board[i][j-1] == word[0]: 
                if self.existhelper(board, word[1:], i, j-1) == 1:
                    return 1

            if j < len(board[0])-1 and board[i][j+1] == word[0]:
                if self.existhelper(board, word[1:], i, j+1) == 1:
                    return 1

            if i > 0 and board[i-1][j] == word[0]:
                if self.existhelper(board, word[1:], i-1, j) == 1:
                    return 1

            if i < len(board)-1 and board[i+1][j] == word[0]:
                if self.existhelper(board, word[1:], i+1, j) == 1:
                    return 1

            return 0

            #return 1
