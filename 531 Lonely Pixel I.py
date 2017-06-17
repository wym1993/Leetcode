class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if not picture or not picture[0]:
            return 0;
        m = len(picture)
        row = {};
        n = len(picture[0]);
        col = [0 for _ in range(n)];
        
        for i in range(m):
            rowCount = []
            for j in range(n):
                if picture[i][j]=='B':
                    rowCount.append(j);
                    col[j]+=1;
                
            if len(rowCount)==1:
                row[i] = rowCount[0];
        
        result = 0;
        for i, j in row.items():
            if col[j]==1:
                result+=1;
    
        return result;
        
        
        