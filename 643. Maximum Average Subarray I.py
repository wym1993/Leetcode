class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        P = [0];
        for i, num in enumerate(nums):
            P.append(P[-1]+num);
        
        return max([P[i+k]-P[i] for i in range(len(nums)-k+1) ])/float(k);
    