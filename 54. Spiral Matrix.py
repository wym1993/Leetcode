class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return [];
        result = [];
        left = 0;
        up = 0;
        down = len(matrix[0])-1;
        right = len(matrix)-1;
        direct = 0;
        
        while True:
            if direct ==0:
                for i in range(up, down+1):
                    result.append(matrix[left][i]);
                left+=1;
            if direct==1:
                for i in range(left, right+1):
                    result.append(matrix[i][down]);
                down = down-1;
            if direct==2:
                for i in range(down, up-1, -1):
                    result.append(matrix[right][i]);
                right = right-1;
            if direct==3:
                for i in range(right, left-1, -1):
                    result.append(matrix[i][up]);
                up+=1;
            
            if left>right or up>down:
                return result;
            direct = (direct+1)%4;