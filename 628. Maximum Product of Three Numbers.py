import itertools
import sys
import operator
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = -sys.maxint;
        
        nums.sort();
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
