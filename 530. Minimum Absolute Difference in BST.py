# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node, left, right, res):
            
            val = node.val;
            res[0] = min(res[0], val-left, right-val);
            
            if node.left:
                dfs(node.left, left, min(right, val), res);
            
            if node.right:
                dfs(node.right, max(left, val), right, res);
        
        res = [sys.maxint]
        dfs(root, -sys.maxint, sys.maxint, res);
        return res[0];
        