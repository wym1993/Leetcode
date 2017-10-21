class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0;
    
        store = [i for i in range(n+1)]
        
        for i in range(2, n+1):
            for j in range(i-1, 1, -1):
                if i%j==0:
                    store[i] = store[j] + i/j;
                    break;
        return store[-1]