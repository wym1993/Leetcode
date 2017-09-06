class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        
        def dfs(cands, tmp):
            if not cands:
                return tmp;
            
            for idx, cand in enumerate(cands):
                cand_bin = bin(cand)[2:]
                cand_bin = '0'*(n-len(cand_bin))+cand_bin
                last_bin = bin(tmp[-1])[2:];
                last_bin = '0'*(n-len(last_bin))+last_bin
                #print tmp, cands, cand, cand_bin, tmp[-1],last_bin, [i!=j for i, j in zip(cand_bin, last_bin)], sum([i!=j for i, j in zip(cand_bin, last_bin)])
                if sum([i!=j for i, j in zip(cand_bin, last_bin)])==1:
                    result = dfs(cands[:idx]+cands[idx+1:], tmp+[cand])
                    if result:
                        return result;
            return None;
    
        return dfs(range(1, 2**n), [0]);
                    
                
def grayCode(self, n):
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)]
        return results