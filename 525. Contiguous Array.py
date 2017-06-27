class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zCount = 0;
        oCount = 0;
        store = {0:-1};
        result = 0;
        for i, num in enumerate(nums):
            if num==0:
                zCount+=1;
            else:
                oCount+=1;
            # zCount+=1 if num==0 else oCount+=1;
            wanted = oCount-zCount;
            if wanted in store:
                index = store[wanted];
                result = max(result, i-index);
            else:
                store[wanted] = i;
        
        return result;