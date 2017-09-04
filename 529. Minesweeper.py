class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def dfs(i, j, board):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return board;
            if board[i][j] == 'E':
                direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1,1)];
                t = sum(board[i+row][j+col]=='M' for row, col in direction if 0<=i+row<len(board) and 0<=j+col<len(board[0]));
                board[i][j] = 'B' if not t else str(t);
                if board[i][j]=='B':
                    for row, col in direction:
                        dfs(i+row, j+col, board);
            return board;
            
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X';
            return board;
        elif board[i][j] == 'B':
            return board;
        else:
            return dfs(i, j, board)
            
        