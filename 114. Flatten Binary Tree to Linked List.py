# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        dummy = root;
        while dummy:
            if dummy.left:
                r = dummy.left;
                while r.right:
                    r = r.right;
                r.right = dummy.right;
                dummy.right = dummy.left;
                dummy.left = None;
            dummy = dummy.right;
        