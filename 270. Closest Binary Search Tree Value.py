import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        store = [root];
        result = sys.maxint;
        while store:
            tmp = store[0];
            store = store[1:];
            if abs(tmp.val-target)<abs(result-target):
                result = tmp.val;
            if tmp.left:
                store.append(tmp.left);
            if tmp.right:
                store.append(tmp.right);
        return result;