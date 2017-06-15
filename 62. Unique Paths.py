
# First
board = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(n):
            board[0][i] = 1
        
        for i in range(m):
            board[i][0] = 1;
        
        for i in range(1,m):
            for j in range(1,n):
                board[i][j] = board[i-1][j]+board[i][j-1];
        
        return board[-1][-1]


# Second
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        board = [0 for _ in range(n)];
        
        board[0] = 1
        for _ in range(m):
            for i in range(1,n):
                board[i]+= board[i-1]
        
        return board[-1]