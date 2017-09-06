class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        cands = [('', range(1, n+1))];
        for _ in range(n):
            next_cands = [];
            for tmp, cand in cands:
                for i, num in enumerate(cand):
                    next_cands.append((tmp+str(num), cand[:i]+cand[i+1:]));
            
            cands = next_cands;
        
        return cands[k-1][0];


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(n):
            num = 1;
            for i in range(1,n+1):
                num*=i;
            return num;
        
        result = ''
        cands = range(1,n+1)
        left, level = k, 0
        while cands:
            num = factorial(n-level-1);
            idx = 0;
            while (idx+1)*num<left:
                idx+=1;
            result+=str(cands[idx]);
            left-=idx*num;
            level+=1;
            del cands[idx];
        
        return result
            
        
        