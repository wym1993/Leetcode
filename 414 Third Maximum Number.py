class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0;
        
        result = list(set(nums))
        if len(result)<3:
            return max(result)
            
        return sorted(result)[-3]