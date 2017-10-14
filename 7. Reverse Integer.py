class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = x
        if n == 0:
            return 0
            
        neg = 1
        if n < 0:
            neg, n = -1, -n
        
        reverse = 0
        while n > 0:
            reverse = reverse * 10 + n % 10
            n = n / 10
        
        reverse = reverse * neg
        if reverse < -(1 << 31) or reverse > (1 << 31) - 1:
            return 0
        return reverse