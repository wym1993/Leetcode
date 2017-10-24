import sys
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        s0, s1 = 0, -sys.maxint;
        
        for i in range(len(prices)):
            tmp = s0;
            s0 = max(s0, s1+prices[i]-fee);
            s1 = max(s1, tmp-prices[i]);
        return s0