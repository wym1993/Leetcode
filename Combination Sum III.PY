from itertools import combinations
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return [cand for cand in combinations(range(1,10), k) if sum(cand)==n];


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = [];
        
        def dfs(tmp, k, n):
            if k==0:
                if sum(tmp)==n:
                    result.append(tmp);
                return;
            
            start = 1 if not tmp else max(tmp)+1
            for i in range(start,10):
                if i in tmp or sum(tmp)+i>n:
                    continue;
                
                dfs(tmp+[i], k-1, n);
            
            return;
    
        dfs([], k, n);
        return result;