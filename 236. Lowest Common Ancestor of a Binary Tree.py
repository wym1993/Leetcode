# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root];
        parent = {root:None};
        while not p in parent or not q in parent:
            node = stack.pop();
            if node.left:
                parent[node.left] = node;
                stack.append(node.left);
            if node.right:
                parent[node.right] = node;
                stack.append(node.right);
        
        ancestor = set();
        while p:
            ancestor.add(p);
            p = parent[p];
        while q not in ancestor:
            q = parent[q];
        return q;
        
        