class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        store = [];
        if sum(nums)%2!=0:
            return False;
        target = sum(nums)/2;
        for num in nums:
            if num in store or num==target:
                return True;
            else:
                new_store = [];
                for item in store:
                    if item>num:
                        new_store.append(item-num)
                    else:
                        new_store.append(item);
                new_store.append(target-num);
                store = new_store[:]
                
        return False;