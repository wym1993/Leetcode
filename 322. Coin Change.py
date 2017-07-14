import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0;
        if not coins or amount<min(coins):
            return -1;
        
        result = [sys.maxint for _ in range(amount+1)]
        for coin in coins:
            if coin<=amount:
                result[coin] = 1;
        
        for i in range(1,amount+1):
            if result[i]==sys.maxint:
                continue;
            
            for coin in coins:
                if i+coin<=amount:
                    result[i+coin] = min(result[i+coin], result[i]+1);
        
        return result[-1] if result[-1]!=sys.maxint else -1;