# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = [];
        def dfs(root):
            if root==None:
                return;
            
            dfs(root.left);
            result.append(root.val);
            dfs(root.right);
        
            return;
        
        dfs(root);
        return result;