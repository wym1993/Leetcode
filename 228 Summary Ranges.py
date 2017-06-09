class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = [];
        if not nums:
            return [];
        
        start = nums[0];
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if start!=nums[i-1]:
                    result.append(str(start)+"->"+str(nums[i-1]));
                else: result.append(str(start));
                start = nums[i];
            
        if start!=nums[-1]:
            result.append(str(start)+"->"+str(nums[-1]));
        else:
            result.append(str(start));
        
        return result;
        