class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return [];
            
        result = [];
        for i in range(n):
            result.append([]);
            for j in range(n):
                result[i].append(0);
        
        left = 0;
        up = 0;
        down = len(result[0])-1;
        right = len(result)-1;
        index = 1;
        direct = 0;
        
        while True:
            if direct==0:
                for i in range(up, down+1):
                    result[left][i] = index;
                    index+=1;
                left+=1;
            if direct==1:
                for i in range(left, right+1):
                    result[i][down] = index;
                    index+=1;
                down = down-1;
            if direct==2:
                for i in range(down, up-1, -1):
                    result[right][i] = index;
                    index+=1;
                right = right-1;
            if direct==3:
                for i in range(right, left-1, -1):
                    result[i][up] = index;
                    index+=1;
                up+=1;
            
            if left>right or up>down:
                return result;
            direct = (direct+1)%4;