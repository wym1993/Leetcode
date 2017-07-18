# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False;
        return self.getSum(root, 0, sum);

    def getSum(self, root, tmp, sum):
        if not root:
            return False;
        if not root.left and not root.right:
            return (tmp+root.val)==sum;
        else:
            return self.getSum(root.left, tmp+root.val, sum) or self.getSum(root.right, tmp+root.val, sum)
            
        