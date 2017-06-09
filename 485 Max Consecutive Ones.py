class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0;
            
        start = 0
        maxLen = 0
        for i, num in enumerate(nums):
            if num!=1:
                if i-start>maxLen:
                    maxLen = i-start;
                start = i+1;
            
        if len(nums)-start>maxLen:
            maxLen = len(nums)-start
        
        return maxLen;