class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        store = []
        if not grid or not grid[0]:
            return 0;

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    nodes = self.dfs(grid, i, j);
                    sortedNodes = sorted(nodes);
                    [x0, y0] = sortedNodes[0]
                    pattern = [[x-x0, y-y0] for [x, y] in sortedNodes[1:]]
                    pattern = sorted(pattern+[[0, 0]]);
                    if not pattern in store:
                        store.append(pattern);

        return len(store);
    
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
            return [];
        tmp = [[i, j]];
        grid[i][j] = -1
        tmp+=self.dfs(grid, i+1, j)
        tmp+=self.dfs(grid, i-1, j)
        tmp+=self.dfs(grid, i, j+1)
        tmp+=self.dfs(grid, i, j-1)
        return tmp