# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        def findRoot(s, t):
            store = [s];
            while store:
                node = store[0];
                store = store[1:];
                if node.val==t.val:
                    yield node;
                    
                if node.left:
                    store.append(node.left);
                if node.right:
                    store.append(node.right);
        
        newS_list = findRoot(s, t);
        if not newS_list:
            return False;
    
        def checkSame(s, t):
            if s and t:
                return checkSame(s.left, t.left) and checkSame(s.right, t.right) and s.val==t.val;
            return s==t;
        
        for newS in newS_list:
            if checkSame(newS,t):
                return True
        return False;
                    
        