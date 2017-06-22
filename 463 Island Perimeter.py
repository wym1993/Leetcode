class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and i==0:
                    result+=1;
                if grid[i][j]==1 and j==0:
                    result+=1;
                
                if j==len(grid[0])-1:
                    if grid[i][j]==1:
                        result+=1;
                else:
                    if grid[i][j]!=grid[i][j+1]:
                        result+=1;
                
                if i==len(grid)-1:
                    if grid[i][j]==1:
                        result+=1;
                else:
                    if grid[i][j]!=grid[i+1][j]:
                        result+=1;
        
        return result;
                    