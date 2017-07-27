# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0;
        
        stack = [(root, 1)];
        mLevel, mVal = 0, 0;
        while stack:
            node, level = stack.pop(0);
            if node.left:
                stack.append((node.left, level+1));
            if node.right:
                stack.append((node.right, level+1));
            if level>mLevel:
                mLevel, mVal = level, node.val;
            # print level, node.val, mLevel, mVal
            
        return mVal;
        