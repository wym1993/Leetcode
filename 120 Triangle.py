class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        r = len(triangle);
        c = len(triangle[-1]);
        board = [[0 for _ in range(c)] for _ in range(r)];
        
        board[0][0] = triangle[0][0];
        if r ==1:
            return board[0][0];
        
        board[1][0] = board[0][0]+triangle[1][0];
        board[1][1] = board[0][0]+triangle[1][1];
        
        for i in range(2, r):
            for j in range(i+1):
                if j==0:
                    board[i][0] = board[i-1][0]+triangle[i][0];
                elif j==i:
                    board[i][j] = board[i-1][j-1]+triangle[i][j];
                else:
                    board[i][j] = min(board[i-1][j], board[i-1][j-1])+triangle[i][j];
        
        # print board
        return min(board[-1]);