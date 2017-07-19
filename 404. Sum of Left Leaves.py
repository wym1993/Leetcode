# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0;
        result = 0;
        store = [(root, False)];
        while store:
            node, isLeaf = store[0];
            store = store[1:];
            if not node.left and not node.right and isLeaf:
                result+=node.val;
                continue;
            if node.left:
                store.append((node.left, True));
            if node.right:
                store.append((node.right, False));
        
        return result;


class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root: return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)   # isn't leave        