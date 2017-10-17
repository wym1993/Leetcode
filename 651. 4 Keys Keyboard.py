class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N<4:
            return N;
        
        dp = [i for i in range(N+1)]
        
        for i in range(4, N+1):
            for j in range(1, i-2):
                dp[i] = max(dp[i], dp[j]*(i-j-1))
        
        return dp[-1]