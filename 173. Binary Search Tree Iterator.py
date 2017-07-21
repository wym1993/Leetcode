# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.store = [];
        self.getInorder(root);
        
    def getInorder(self, root):
        if not root:
            return;
        self.getInorder(root.left);
        self.store.append(root.val);
        self.getInorder(root.right);
        return;
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.store;
        

    def next(self):
        """
        :rtype: int
        """
        result = self.store[0];
        self.store = self.store[1:]
        return result;
    
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = list()
        self.pushAll(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val
        
    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left