class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0;
        '''
        n = len(s);
        dp = [[0]*n for _ in range(n)];
        
        for j in range(n):
            for i in range(j, -1, -1):
                if i==j:
                    dp[i][j]=1;
                    continue;
                
                if s[i]==s[j]:
                    if j-i==1:
                        dp[i][j] = 2;
                    else:
                        dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
        
        #print dp
        return dp[0][-1]
        '''
        
        n = len(s)
        dp = [1] * n
        for j in xrange(1, len(s)):
            pre = dp[j]
            for i in reversed(xrange(0, j)):
                tmp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                pre = tmp
        return dp[0]