class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str 
        :rtype: int
        """
        if len(s)==0:
            return 0;
        n = len(s)
        
        dp = [[False]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i]==s[j] and (j-i<3 or dp[i+1][j-1])
        
        return sum([sum(row) for row in dp]);