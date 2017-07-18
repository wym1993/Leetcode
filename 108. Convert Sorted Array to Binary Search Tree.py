# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.getTree(nums);

    def getTree(self, nums):
        if not nums:
            return None;
        mid = len(nums)/2;
        root = TreeNode(nums[mid]);
        root.left = self.getTree(nums[:mid]);
        root.right = self.getTree(nums[mid+1:]);
        return root;