# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None;
        
        def formTree(t1, t2):
            if not t1 and not t2:
                return None;
            num1 = t1.val if t1 else 0;
            num2 = t2.val if t2 else 0;
            root = TreeNode(num1+num2);
            t1_left = t1.left if t1 else None;
            t1_right = t1.right if t1 else None;
            t2_left = t2.left if t2 else None;
            t2_right = t2.right if t2 else None;
            root.left = formTree(t1_left, t2_left);
            root.right = formTree(t1_right, t2_right);
            return root;
        
        return formTree(t1, t2);
            
        