# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return None;
        result = [];
        store = [(root, 0)];
        
        while store:
            node,level = store[0];
            store = store[1:];
            if len(result)<=level:
                result.append([node.val]);
            else:
                result[level].append(node.val);
            
            if node.left:
                store.append((node.left, level+1));
            if node.right:
                store.append((node.right, level+1));
        
        return [sum(l)*1.0/len(l) for l in result];