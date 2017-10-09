class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return [];
        
        m, n = len(matrix), len(matrix[0])
        p_visit = [[False for _ in range(n)] for _ in range(m)];
        a_visit = [[False for _ in range(n)] for _ in range(m)];
        
        def dfs(matrix, i, j, visited):
            
            visited[i][j] = True
            for dir in [(1,0),(-1,0),(0,1),(0,-1)]:
                x, y = i + dir[0], j + dir[1]
                if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or visited[x][y] or matrix[x][y] < matrix[i][j]:
                    continue
                dfs(matrix, x, y, visited)
        
        for i in range(m):
            dfs(matrix, i, 0, p_visit);
            dfs(matrix, i, n-1, a_visit);
        
        for j in range(n):
            dfs(matrix, 0, j, p_visit);
            dfs(matrix, m-1, j, a_visit);
        
        result = [];
        for i in range(m):
            for j in range(n):
                if p_visit[i][j] and a_visit[i][j]:
                    result.append([i, j]);
        return result;