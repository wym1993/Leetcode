class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [];
        
        def dfs(nums, visit, tmp):
            if len(tmp)==len(nums):
                if tmp not in result:
                    result.append(tmp);
                return;
            
            for i, item in enumerate(nums):
                if i in visit:
                    continue;
                
                dfs(nums, visit+[i], tmp+[item]);
            
            return;
            
        
        nums.sort();
        dfs(nums, [], []);
        return result;


class Solution(object):
    def permute(self, nums):
        return [[n] + p for i, n in enumerate(nums) for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
        

    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)