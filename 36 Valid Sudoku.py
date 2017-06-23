class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    if not self.checkRow(board, i, j) or not self.checkColumn(board, i, j) or not self.checkSquare(board, i, j):
                        return False;
        return True;
    
    def checkRow(self, board, i, j):
        num = board[i][j]
        for k in range(len(board[i])):
            if k!=j:
                if board[i][k]==num:
                    print "row" + str(k)
                    return False;
        
        return True;
    
    def checkColumn(self, board, i, j):
        num = board[i][j];
        for k in range(len(board)):
            if k!=i:
                if board[k][j]==num:
                    print "column" + str(k)
                    return False;
        
        return True;
    
    def checkSquare(self, board, i, j):
        rowSquare = i/3;
        columnSquare = j/3;
        
        for k in range(rowSquare*3, rowSquare*3+3):
            for l in range(columnSquare*3, columnSquare*3+3):
                if k!=i or l!=j:
                    if board[k][l]==board[i][j]:
                        print "square"+str(i) + str(j) + str(board[i][j]) + ' '+ str(k) + str(l) + str(board[k][l]) + " " + str(board[i][j]==board[k][l]);
                        return False;
        
        return True;
        