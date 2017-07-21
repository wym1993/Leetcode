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
        nodes = [root];
        
        while nodes:
            next_nodes = [];
            for i, node in enumerate(nodes):
                if i==len(nodes)-1:
                    node.next = None;
                else:
                    node.next = nodes[i+1];
                if node.left:
                    next_nodes.append(node.left);
                if node.right:
                    next_nodes.append(node.right);
            nodes = next_nodes;
            
        
        
        