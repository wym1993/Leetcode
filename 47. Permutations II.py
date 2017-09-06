class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(cand, tmp, nums):
            if len(tmp)==len(nums):
                result.append(tmp);
                return;
            
            for num in set(cand):
                idx = cand.index(num);
                dfs(cand[:idx]+cand[idx+1:], tmp+[num], nums);
        
        dfs(nums, [], nums);
        return result;
        