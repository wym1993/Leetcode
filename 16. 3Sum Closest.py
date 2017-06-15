class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums)<3:
            return target;
            
        nums.sort();    
        result = sys.maxint
        
        for i in range(len(nums)):
            j = i+1;
            k = len(nums)-1;
            while j<k:
                s = nums[i]+nums[j]+nums[k];
                if s==target:
                    return s;
                
                if abs(s-target)<abs(result-target):
                    result = s;
                
                if s<target:
                    j+=1;
                else:
                    k-=1;
        
        return result;