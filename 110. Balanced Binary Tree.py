# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.getDepth(root)!=-1
    
    def getDepth(self, root):
        if not root:
            return 0;
        left = self.getDepth(root.left);
        right = self.getDepth(root.right);
        if left==-1 or right == -1 or abs(left-right)>1:
            return -1;
        return 1+max(left, right);
