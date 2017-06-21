class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True] * max(n, 2)
        isPrime[0], isPrime[1] = False, False
        x = 2
        while x *2 < n:
            if isPrime[x]:
                p = x * 2
                while p < n:
                    isPrime[p] = False
                    p += x
            x += 1
        return sum(isPrime)
                
    
    
    