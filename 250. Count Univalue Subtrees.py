# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0;
        self.result = 0;
        
        def findSubtree(root):
            if not root.left and not root.right:
                self.result+=1;
                return {root.val};
            
            left = findSubtree(root.left) if root.left else set();
            right = findSubtree(root.right) if root.right else set();
            tmp = left|right|{root.val};
            if len(tmp)==1:
                self.result+=1;
            return tmp;
        
        findSubtree(root);
        return self.result;