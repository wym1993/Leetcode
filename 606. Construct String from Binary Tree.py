# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return "";
        
        left = self.tree2str(t.left);
        right = self.tree2str(t.right);
        if not left and not right:
            return str(t.val);
        result = str(t.val)+'('+left+')';
        if right:
            result+='('+right+')';
        return result;
        