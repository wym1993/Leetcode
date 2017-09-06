class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = [];
        
        def dfs(cands, tmp, k):
            if len(tmp)==k:
                result.append(tmp);
                return;
            
            for i, cand in enumerate(cands):
                dfs(cands[i+1:], tmp+[cand], k);
            
            return;
    
        dfs(range(1,n+1), [], k);
        return result;


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = [];
        cands = range(1, n+1);
        
        for num in range(2**n):
            if bin(num)[2:].count('1') == k:
                store = '0'*(n-len(bin(num)[2:]))+bin(num)[2:]
                result.append([cands[i] for i, c in enumerate(store) if c=='1']);
        
        return result;

class Solution:
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(1, n+1) for pre in self.combine(i-1, k-1)]