class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final = 0
        nums = sorted(nums)
        for i in range(2,len(nums))[::-1]:
            l = 0
            r = i-1
            while (r>l):
                if nums[l]+nums[r] > nums[i]:
                    final += r-l
                    r-=1
                else:
                    l+=1
        return final