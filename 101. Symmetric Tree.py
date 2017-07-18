# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True;
        return self.checkTree(root.left, root.right);

    def checkTree(self, p, q):
        if p and q:
            return p.val==q.val and self.checkTree(p.left, q.right) and self.checkTree(p.right, q.left);
        return p is q