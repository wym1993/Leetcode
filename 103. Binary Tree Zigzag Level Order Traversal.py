# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return [];
        
        result, store = [], [(root, 0)];
        while store:
            (node, level), store = store[0], store[1:];
            if len(result)<=level:
                result.append([node.val]);
            else:
                if level%2==1:
                    result[level].insert(0, node.val);
                else:
                    result[level].append(node.val);
            
            if node.left:
                store.append((node.left, level+1));
            if node.right:
                store.append((node.right, level+1));
        
        return result;