class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1:
            return 0;
        if n==1:
            return 1;
        if n==2:
            return 2;
            
        kind = [0,1,2];
        for i in range(3,n+1):
            kind[i%3] = kind[(i-1)%3] + kind[(i-2)%3]
        
        return kind[n%3]