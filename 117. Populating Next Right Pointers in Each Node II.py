# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return;
        prev, curr = root, None;
        while prev:
            prev, curr = None, prev;     
            
            while curr:
                if not curr.left and not curr.right:
                    curr = curr.next;
                    continue;
                
                if not prev:
                    prev = curr.left if curr.left else curr.right;

                if curr.left and curr.right:
                    curr.left.next = curr.right;
                    
                t = curr.left if not curr.right else curr.right;
                f = curr.next;
                while f and (not f.left and not f.right):
                    f = f.next;

                if f:
                    t.next = f.left if f.left else f.right;
                    curr = f;
                else:
                    curr = None;
        
        