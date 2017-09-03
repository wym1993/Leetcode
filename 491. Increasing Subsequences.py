class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [];
        
        def dfs(tmp, i, nums):
            if i==len(nums):
                if not tmp in result and len(tmp)>1:
                    result.append(tmp)
                return;
            
            if not tmp or nums[i]>=tmp[-1]:
                dfs(tmp+[nums[i]], i+1, nums);

            dfs(tmp, i+1, nums);
            return;
    
        dfs([], 0, nums);
        return result;
	
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = {()}
        for num in nums:
            subs |= {sub + (num,)
                     for sub in subs
                     if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]