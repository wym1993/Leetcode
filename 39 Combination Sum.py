class Solution(object):
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = list(set(candidates))
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret

    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            Solution.ret.append(valuelist)
            return
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])

        