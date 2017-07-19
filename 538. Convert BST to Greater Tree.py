# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None;
        
        self.inorder_list = []
        def inorder(root):
            if not root:
                return;
            
            inorder(root.left);
            self.inorder_list.append(root.val);
            inorder(root.right);
            return;
        
        def getSum(root):
            if not root:
                return;
            idx = self.inorder_list.index(root.val);
            # print root.val, idx, sum(self.inorder_list[idx:])
            root.val = sum(self.inorder_list[idx:]);
            getSum(root.left);
            getSum(root.right);
            return;
    
        inorder(root);
        # print self.inorder_list
        getSum(root);
        return root;
        