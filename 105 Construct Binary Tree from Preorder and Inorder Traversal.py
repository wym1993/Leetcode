# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # if not preorder or not inorder:
        #     return None
        # root = TreeNode(preorder[0]);
        # i = 1;
        # while i<len(preorder) and inorder.index(preorder[i])<inorder.index(preorder[0]):
        #     i+=1;
        # left = preorder[1:i];
        # right = preorder[i:];
        # def findNext(node, preorder, inorder, left, right):
        #     if not left and not right:
        #         return;
        #     if left:
        #         node.left = TreeNode(left[0]);
        #         i = 1;
        #         while i<len(left) and inorder.index(left[i])<inorder.index(left[0]):
        #             i+=1;
        #         findNext(node.left, preorder, inorder, left[1:i], left[i:]);
            
        #     if right:
        #         node.right = TreeNode(right[0]);
        #         i=1;
        #         while i<len(right) and inorder.index(right[i])<inorder.index(right[0]):
        #             i+=1;
        #         findNext(node.right,preorder, inorder, right[1:i], right[i:]);
            
        #     return;
        
        # findNext(root, preorder, inorder, left, right);
        # return root;
        # if not preorder or not inorder:
        #     return None
        
        # root = TreeNode(preorder[0]);
        # waited = [root]
        # while len(waited)!=0:
        #     node = waited[0];
        #     del waited[0];
        #     # visited.append(node.val);
        #     # left = preorder.index(node.val)+1;
        #     idx = preorder.index(node.val);
        #     right = idx+1;
        #     while right<len(preorder) and inorder.index(preorder[right])<inorder.index(preorder[idx]):
        #         right+=1;
        #     if preorder[(idx+1):right]:
        #         node.left = TreeNode(preorder[idx+1]);
        #         waited.append(node.left);
                
        #     if right<len(preorder):
        #         node.right = TreeNode(preorder[right]);
        #         waited.append(node.right);
        
        # return root;
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0]);
        rootPos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : 1 + rootPos], inorder[ : rootPos])
        root.right = self.buildTree(preorder[rootPos + 1 : ], inorder[rootPos + 1 : ])
        return root;
            
        