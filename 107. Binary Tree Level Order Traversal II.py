# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
result = []

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        global result;
        result = [];
        self.checkTree(root, 1);
        return result[::-1];
    
    def checkTree(self, root, level):
        if not root:
            return;
        if len(result)<level:
            result.append([root.val]);
        else:
            result[level-1].append(root.val)
        self.checkTree(root.left, level+1);
        self.checkTree(root.right, level+1);


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return [];
        
        store = [(root, 1)];
        result = []
        while store:
            node, level = store[0];
            store = store[1:];
            if len(result)<level:
                result.append([node.val]);
            else:
                result[level-1].append(node.val);
            if node.left:
                store.append((node.left, level+1));
            if node.right:
                store.append((node.right, level+1));
        
        return result[::-1];
        
        