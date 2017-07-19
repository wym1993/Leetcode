# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0;
        def getDia(root):
            if not root:
                return 0;
            left = getDia(root.left);
            right = getDia(root.right);
            self.result = max(self.result, left+right);
            return max(left, right)+1;
        
        getDia(root);
        return self.result;
        
        