import sys
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if not bank:
            return -1;
        
        def calcDis(num1, num2):
            return sum([c1!=c2 for c1, c2 in zip(num1, num2)])==1
        
        def dfs(cands, curr, end, step):
            #print cands, curr, step
            if curr==end:
                return step;
            
            store = []
            for i, cand in enumerate(cands):
                if calcDis(curr, cand):
                    res = dfs(cands[:i]+cands[i+1:], cand, end, step+1);
                    if res!=-1:
                        store.append(res);
            
            if not store:
                return -1;
            else:
                return min(store)
    
        return dfs(bank, start, end, 0)