# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return [];
        
        def dfs(root):
            if not root:
                return 0;
            s = root.val+dfs(root.left)+dfs(root.right);
            store[s]+=1;
            return s;
        
        store = Counter();
        dfs(root);
        frequent = max(store.values());
        return [s for s in store.keys() if store[s]==frequent];