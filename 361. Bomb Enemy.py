class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0;
        
        m, n = len(grid), len(grid[0]);
        row = 0
        col = [0]*n
        res = 0;
        
        for i in range(m):
            for j in range(n):
                if j==0 or grid[i][j-1]=='W':
                    row = 0;
                    for k in range(j, n):
                        if grid[i][k]=='W':
                            break;
                        else:
                            row+=grid[i][k]=='E';
                if i==0 or grid[i-1][j]=='W':
                    col[j] = 0;
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break;
                        else:
                            col[j]+=grid[k][j]=='E';
                
                if grid[i][j]=='0':
                    res = max(res, row+col[j]);
        
        return res;