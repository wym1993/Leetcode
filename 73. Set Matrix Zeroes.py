class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        c = [];
        r = [];
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    if not i in r:
                        r.append(i);
                    if not j in c:
                        c.append(j);
        
        for i in range(len(matrix)):
            if i in r:
                matrix[i] = [0 for _ in range(len(matrix[i]))];
                continue;
            for j in range(len(matrix[i])):
                if j in c:
                    matrix[i][j] = 0;
            