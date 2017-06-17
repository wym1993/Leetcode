class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return [];
        candidates.sort();
        self.result = [];
        self.dfs(candidates, target, []);
        return self.result;
    
    def dfs(self, candidates, target, valuelist):
        if target==0:
            # if not valuelist in self.result:
            self.result.append(valuelist);
            return;
        
        for i, candidate in enumerate(candidates):
            if i>=1 and candidates[i]==candidates[i-1]:
                continue;
            if target>=candidate:
                self.dfs(candidates[i+1:], target-candidate, valuelist+[candidate]);
        
        return;