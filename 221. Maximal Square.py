class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0;
        
        store = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))];
        maxR = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        store[i][j] = 1;
                    else:
                        store[i][j] = min(store[i-1][j], store[i-1][j-1], store[i][j-1])+1;
                
                maxR = max(maxR, store[i][j])
        
        return maxR**2;
                    
                
                
                