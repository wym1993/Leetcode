class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False;
        
        if not word:
            return True
        
        def dfs(x, y, word):
            if not word:
                return True;
            
            if x!=0 and board[x-1][y]==word[0]:
                tmp = board[x][y];
                board[x][y] = '*'
                if dfs(x-1, y, word[1:]):
                    return True;
                board[x][y] = tmp
            
            if x<len(board)-1 and board[x+1][y] ==word[0]:
                tmp = board[x][y];
                board[x][y] = '*'
                if dfs(x+1, y, word[1:]):
                    return True;
                
                board[x][y] = tmp
            
            if y!=0 and board[x][y-1]==word[0]:
                tmp = board[x][y];
                board[x][y] = '*'
                if dfs(x,y-1, word[1:]):
                    return True;
                board[x][y] = tmp
            
            if y<len(board[0])-1 and board[x][y+1]==word[0]:
                tmp = board[x][y];
                board[x][y] = '*'
                if dfs(x,y+1, word[1:]):
                    return True;
                board[x][y] = tmp
        
            return False;
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if dfs(i, j, word[1:]):
                        return True;
                
        return False;