class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0];
        
        return max(self.roblinear(nums[1:]), self.roblinear(nums[:-1]));
    
    def roblinear(self, nums):
        size = len(nums);
        even, odd = 0, 0;
        for i in range(size):
            if i%2:
                odd = max(odd + nums[i], even);
            else:
                even = max(even + nums[i], odd);
        
        return max(even, odd);