from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0;
        
        store = defaultdict(int);
        store[0] = 1
        count, cumu = 0, 0
        for num in nums:
            cumu+=num;
            count+=store[cumu-k];
            
            store[cumu]+=1
        
        return count;