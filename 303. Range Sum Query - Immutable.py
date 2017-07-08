class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.store = [sum(nums[:i]) for i in range(len(nums)+1)];
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.store[j+1]-self.store[i];
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)