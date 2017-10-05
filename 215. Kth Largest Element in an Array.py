import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        A = [];
        heapq.heappush(A, nums);
        return heapq.nlargest(k, A)[-1][k-1]