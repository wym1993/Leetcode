from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nCounter = Counter(nums);
        result = 0;
        num_keys = sorted(nCounter.keys());
        for i in range(1, len(num_keys)):
            if num_keys[i]-num_keys[i-1]>1:
                continue;
            if nCounter[num_keys[i]]+nCounter[num_keys[i-1]]>result:
                result = nCounter[num_keys[i]]+nCounter[num_keys[i-1]]
        
        return result;