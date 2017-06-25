from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        store = Counter(nums);
        return [key for key, val in store.most_common(k)];
        
        