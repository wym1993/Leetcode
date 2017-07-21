# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return [];
        result = []
        store = [(root, 0)];
        
        while store:
            node, level = store[0];
            store = store[1:];
            if len(result)<=level:
                result.append(node.val);
            else:
                result[level] = node.val;
            
            if node.left:
                store.append((node.left, level+1));
            if node.right:
                store.append((node.right, level+1));
        
        return result;
        
        