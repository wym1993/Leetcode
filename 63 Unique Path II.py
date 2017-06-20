import sys
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0;
        
        r = len(obstacleGrid);
        c = len(obstacleGrid[0]);
        
        grid = [[0 for _ in range(c)] for _ in range(r)];
        
        for i in range(r):
            if i==0:
                grid[i][0] = int(obstacleGrid[i][0]==0);
            else:
                if obstacleGrid[i][0]==1 or grid[i-1][0]==0:
                    grid[i][0] = 0;
                else:
                    grid[i][0] = 1;
        
        for j in range(c):
            if j==0:
                grid[0][j] = int(obstacleGrid[0][j]==0);
            else:
                if obstacleGrid[0][j]==1 or grid[0][j-1]==0:
                    grid[0][j] = 0;
                else:
                    grid[0][j] = 1;
                # grid[0][j] = int(obstacleGrid[0][j]==0 o);
        
        print grid
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j]==1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j]+grid[i][j-1];
                    
        return grid[-1][-1]