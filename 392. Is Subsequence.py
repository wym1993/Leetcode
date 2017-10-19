class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True;
        if not t:
            return False;
        '''
        m, n = len(s), len(t)
        dp = [[False]*(n+1) for _ in range(2)];
        
        for i in range(n+1):
            dp[0][i] = True;
            
        for i in range(1, m+1):
            for j in range(i, n+1):
                dp[i][j] = dp[i-1][j-1] and (s[i-1]==t[j-1] or dp[i][j-1]);
        
        return dp[-1][-1]
        '''
        
        i, j = 0, 0;
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1;
            j+=1;
        
        return True if i==len(s) else False;
        