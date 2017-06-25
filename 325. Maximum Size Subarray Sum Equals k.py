class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0;
        csum = 0;
        store = {0:0};
        for i, num in enumerate(nums):
            csum+=num;
            wanted = csum-k;
            if wanted in store:
                result = max(result, i+1-store[wanted]);
            
            if csum not in store:
                store[csum] = i+1;
        
        return result or 0;