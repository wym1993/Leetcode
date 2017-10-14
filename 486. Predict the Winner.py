class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return True;
        
        def dfs(res, left, right, op):
            if not res:
                #print left, right
                return left>=right;
            
            if op==0:
                return dfs(res[1:], left+res[0], right, 1) or dfs(res[:-1], left+res[-1], right, 1);
            else:
                return dfs(res[1:], left, right+res[0], 0) and dfs(res[:-1], left, right+res[-1], 0);
        
        return dfs(nums, 0, 0, 0);