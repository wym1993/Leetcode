# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return [];
        
        result = [];
        
        def findSum(node, store, s):
            if not node.left and not node.right:
                if sum(store)+node.val==s:
                    result.append(store+[node.val]);
                return;
            
            if node.left:
                findSum(node.left, store+[node.val], s);
            if node.right:
                findSum(node.right, store+[node.val], s);
        
        findSum(root, [], s);
        return result;
        
                
        