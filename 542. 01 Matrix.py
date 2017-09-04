class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def neighbors(i, j, matrix, step):
            row, col = len(matrix), len(matrix[0]);
            for m, n in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0<=m<row and 0<=n<col:
                    yield ((m, n), step)
        
        row, col = len(matrix), len(matrix[0])
        q = set([((i, j), 0) for i in range(row) for j in range(col) if matrix[i][j]==0]);
        result = [[-1]*col for _ in range(row)];
        while q:
            next_q = set();
            for ((i, j),step) in q:
                if result[i][j]==-1:
                    result[i][j] = step;
                    next_q.update(neighbors(i, j, matrix, step+1));
            
            q = next_q;
            
        
        return result;