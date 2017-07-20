import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def checkValid(node, left, right):
            if not node:
                return True;
            
            if node.val<=left or node.val>=right:
                return False;
            
            return checkValid(node.left, left, min(node.val, right)) and checkValid(node.right, max(left, node.val), right);
            
        
        return checkValid(root, -sys.maxint, sys.maxint);


class Solution:
    # @param root, a tree node
    # @return a boolean
    # 7:38
    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if root is None:
            return
        
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
        