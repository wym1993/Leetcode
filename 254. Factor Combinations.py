class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def getFactor(n, i, temp, result):
            while i*i<=n:
                if n%i==0:
                    result.append(temp+[i, n/i]);
                    getFactor(n/i, i, temp+[i], result);
                i+=1;
            
            return result;
        
        return getFactor(n, 2, [], []);
                
        