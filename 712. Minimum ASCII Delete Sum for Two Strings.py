class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2);
        dp = [[0]*(n+1) for _ in range(m+1)];

        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0]+ord(s1[i-1]);
        for i in range(1, n+1):
            dp[0][i] = dp[0][i-1]+ord(s2[i-1]);

        for i in range(1, m+1):
            for j in range(1, n+1):
                cost = 0 if s1[i-1]==s2[j-1] else ord(s1[i-1])+ord(s2[j-1])
                dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]), dp[i][j-1]+ord(s2[j-1]), dp[i-1][j-1]+cost);

        return dp[-1][-1]