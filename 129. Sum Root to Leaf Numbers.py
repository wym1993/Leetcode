# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0;
        
        def getSum(root, total):
            result = total+root.val
            if not root.left and not root.right:
                return result;
            
            left =  getSum(root.left, result*10) if root.left else 0;
            right =  getSum(root.right, result*10) if root.right else 0;
            
            return left+right
    
        return getSum(root, 0);
                

# dfs + stack
def sumNumbers1(self, root):
    if not root:
        return 0
    stack, res = [(root, root.val)], 0
    while stack:
        node, value = stack.pop()
        if node:
            if not node.left and not node.right:
                res += value
            if node.right:
                stack.append((node.right, value*10+node.right.val))
            if node.left:
                stack.append((node.left, value*10+node.left.val))
    return res
    