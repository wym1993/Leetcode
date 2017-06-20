# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None;
        root = TreeNode(postorder[-1]);
        rootPos = inorder.index(postorder[-1]);
        right_len = len(inorder)-rootPos;
        root.left = self.buildTree(inorder[:rootPos], postorder[:rootPos]);
        root.right = self.buildTree(inorder[rootPos+1:], postorder[rootPos:-1]);
        return root;