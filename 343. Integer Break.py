class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [i for i in range(n+1)];
        result[-1] = 1
        for i in range(1, n):
            for j in range(i+1, n+1):
                result[j] = max(result[j], result[i]*(j-i));
        
        return result[-1];