class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        count = 0;
        sum = 0;
        for num in nums:
            if sum>=n:
                return count;
            
            while sum<num-1:
                count+=1;
                sum+=sum+1;
                if sum>=n:
                    return count;
            
            sum+=num;
        
        while sum+1<=n:
            count+=1;
            sum+=sum+1;
        
        return count;
                