from collections import Counter
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        '''
        store = {(0, 0):0};
        res = 0;
        
        for str in strs:
            print str
            curr = (str.count('0'), str.count('1'));
            next_store = {}
            for cand in store.keys():
                if cand[0]+curr[0]==m and cand[1]+curr[1]==n:
                    res = max(res, store[cand]+1);
                    continue;
                
                if cand[0]+curr[0]<=m and cand[1]+curr[1]<=n:
                    tmp = (cand[0]+curr[0], cand[1]+curr[1])
                    next_store[tmp] = max(next_store.get(tmp, 0),store.get(tmp, 0), store[cand]+1);
            store.update(next_store);
        
        return res;
        '''
        dp = [[0]*(n+1) for _ in range(m+1)];
        for str in strs:
            z, o = str.count('0'), str.count('1');
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i-z>=0 and j-o>=0:
                        dp[i][j] = max(dp[i][j], 1+dp[i-z][j-o]);
            
        return dp[m][n]
                
        