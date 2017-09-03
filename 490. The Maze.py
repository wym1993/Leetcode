class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        visit = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))];
        
        def dfs(maze, visit, i, j, d_i, d_j):
            if i==d_i and j==d_j:
                return True;
            if visit[i][j] == True:
                return False;
            
            visit[i][j]=True;
            
            #left
            k = i
            while k>=0 and maze[k][j]==0:
                k-=1;
            left = dfs(maze, visit, k+1, j, d_i, d_j) if (k+1, j)!=(i, j) else False;
            
            k = i
            while k<len(maze) and maze[k][j]==0:
                k+=1;
            right = dfs(maze, visit, k-1, j, d_i, d_j) if (k-1, j)!=(i, j) else False;
            
            k = j
            while k>=0 and maze[i][k]==0:
                k-=1;
            up = dfs(maze, visit, i, k+1, d_i, d_j) if (i, k+1)!=(i, j) else False;
            
            k=j
            while k<len(maze[0]) and maze[i][k]==0:
                k+=1;
            down = dfs(maze, visit, i, k-1, d_i, d_j) if (i, k-1)!=(i, j) else False;
        
            return left or right or up or down;
        
        return dfs(maze, visit, start[0], start[1], destination[0], destination[1]);

		
	def hasPath(self, maze, start, destination):

        Q = [start]
        n = len(maze)
        m = len(maze[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        while Q:
            # Use Q.pop() as DFS or Q.popleft() with deque from collections library for better performance. Kudos to @whglamrock
            i, j = Q.pop(0)
            maze[i][j] = 2

            if i == destination[0] and j == destination[1]:
                return True
            
            for x, y in dirs:
                row = i + x
                col = j + y
                while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                    row += x
                    col += y
                row -= x
                col -= y
                if maze[row][col] == 0:
                    Q.append([row, col])
        
        return False