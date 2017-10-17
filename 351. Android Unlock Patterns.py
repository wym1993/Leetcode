from itertools import combinations
class Solution(object):
    def getVal(self, skip, visit, node, remain):
        if remain<0:
            return 0;
        if remain==0:
            return 1;
        
        visit[node] = True;
        tmp = 0;
        for i in range(1, 10):
            if not visit[i] and (skip[node][i]==0 or visit[skip[node][i]]):
                tmp+=self.getVal(skip, visit, i, remain-1);
        visit[node] = False;
        return tmp;
    
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        skip = [[0]*10 for _ in range(10)];
        visit = [False]*10
        skip[1][3] = skip[3][1] = 2;
        skip[1][7] = skip[7][1] = 4;
        skip[3][9] = skip[9][3] = 6;
        skip[7][9] = skip[9][7] = 8;
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5;
        res = 0
        for i in range(m, n+1):
            res+=self.getVal(skip, visit[:], 1, i-1)*4;
            res+=self.getVal(skip, visit[:], 2, i-1)*4;
            res+=self.getVal(skip, visit[:], 5, i-1)
        return res;
        
        