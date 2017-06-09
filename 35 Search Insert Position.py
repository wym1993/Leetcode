class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target);
        
        i=0;
        while i<len(nums) and nums[i]<target:
            i+=1;
        
        return i;