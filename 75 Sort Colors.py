import heapq
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # left = 0;
        # right = len(nums)-1;
        # while True:
        #     while left<len(nums) and nums[left]!=1:
        #         left+=1;
        #     while right>=0 and nums[right]!=0:
        #         right-=1;
        #     if left<right:
        #         nums[left], nums[right] = nums[right], nums[left];
        #     else:
        #         break;
        
        # left = 0;
        # right = len(nums)-1;
        # while True:
        #     while left<len(nums) and nums[left]!=2:
        #         left+=1;
        #     while right>=0 and nums[right]!=1:
        #         right-=1;
        #     if left<right:
        #         nums[left], nums[right] = nums[right], nums[left];
        #     else:
        #         break;
        
        # left = 0;
        # right = len(nums)-1;
        # while True:
        #     while left<len(nums) and nums[left]!=2:
        #         left+=1;
        #     while right>=0 and nums[right]!=0:
        #         right-=1;
        #     if left<right:
        #         nums[left], nums[right] = nums[right], nums[left];
        #     else:
        #         break;
        
        r = 0
        b = len(nums)-1;
        i = 0;
        
        while i<=b:
            print i, r, b
            if nums[i]==0:
                nums[i], nums[r] = nums[r], nums[i]
                r+=1;
                i+=1
                continue;
            if nums[i]==2:
                nums[i], nums[b] = nums[b], nums[i]
                b-=1;
                continue;
            
            i+=1;
        