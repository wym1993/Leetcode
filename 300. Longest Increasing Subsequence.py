class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0;
        result = [0 for _ in range(len(nums))];
        result[-1] = 1;
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == max(nums[i:]):
                result[i] = 1;
            else:
                result[i] = max([result[j] for j in range(i+1, len(nums)) if nums[i]<nums[j]])+1
        return max(result);
        