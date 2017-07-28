# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return None;
        
        if d==1:
            tmp = TreeNode(v);
            tmp.left = root;
            root = tmp;
            return root;
        
        stack = [root];
        level = 1;
        while level<d-1:
            tmp = []
            for node in stack:
                if node.left:
                    tmp.append(node.left);
                if node.right:
                    tmp.append(node.right);
            stack = tmp;
            level+=1;
        
        for node in stack:
            l, r = TreeNode(v), TreeNode(v);
            l.left, node.left = node.left, l;
            r.right, node.right = node.right, r;
        
        return root;


def addOneRow(self, root, v, d):
    dummy, dummy.left = TreeNode(None), root
    row = [dummy]
    for _ in range(d - 1):
        row = [kid for node in row for kid in (node.left, node.right) if kid]
    for node in row:
        node.left, node.left.left = TreeNode(v), node.left
        node.right, node.right.right = TreeNode(v), node.right
    return dummy.left