# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return [];
        stack = [(root, 0)];
        result = [];
        while stack:
            node, level = stack.pop();
            if len(result)<=level:
                result.append(node.val);
            else:
                result[level] = max(result[level], node.val);
            
            if node.left:
                stack.append((node.left, level+1));
            if node.right:
                stack.append((node.right, level+1));
            
        return result;


def largestValues(self, root):
    if not root:
        return []
    left = self.largestValues(root.left)
    right = self.largestValues(root.right)
    return [root.val] + map(max, left, right)
        