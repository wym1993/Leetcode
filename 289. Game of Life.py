class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return;
        m = len(board);
        n = len(board[0]);
        
        for i in range(m):
            for j in range(n):
                nei = sum(board[a][b]%2 for a in range(i-1, i+2) for b in range(j-1, j+2) if 0<=a<m and 0<=b<n)-board[i][j]
                if board[i][j]==0 and nei==3:
                    board[i][j] = 2;
                if board[i][j]==1 and (nei<2 or nei>3):
                    board[i][j] = 3;
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==2:
                    board[i][j]=1;
                if board[i][j]==3:
                    board[i][j]=0
        
        return;
        