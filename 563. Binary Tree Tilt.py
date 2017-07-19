# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0;
        
        self.result = 0;
        
        def calcTilt(root):
            if not root:
                return 0;
            
            left = calcTilt(root.left);
            right = calcTilt(root.right);
            self.result+=abs(left-right);
            return left+right+root.val;
        
        calcTilt(root);
        return self.result;
                