import sys
class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        n_city = len(flights);
        n_week = len(days[0])
        
        dp = [[-sys.maxint]*(n_week+1) for _ in range(n_city)];
        dp[0][0] = 0;
        for j in range(1, n_week+1):
            for i in range(n_city):
                cands = [dp[k][j-1] for k in range(n_city) if k==i or flights[k][i]==1];
                if cands:
                    dp[i][j] = max(cands)+days[i][j-1];

        return max([dp[i][-1] for i in range(n_city)])