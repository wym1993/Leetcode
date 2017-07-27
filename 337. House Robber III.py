# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0;
        
        def robDFS(root):
            if not root:
                return (0, 0);
            l = robDFS(root.left);
            r = robDFS(root.right);
            return (l[1]+r[1], max(l[1]+r[1], l[0]+r[0]+root.val));
        
        return robDFS(root)[1];