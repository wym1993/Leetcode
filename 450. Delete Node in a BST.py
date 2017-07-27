# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None;
        
        if root.val==key:
            if root.left:
                right_most = root.left;
                while right_most.right:
                    right_most = right_most.right;
                right_most.right = root.right;
                return root.left;
            else:
                return root.right;
        
        if root.val<key:
            root.right = self.deleteNode(root.right, key);
        if root.val>key:
            root.left = self.deleteNode(root.left, key);
        
        return root;
        