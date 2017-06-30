# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head==None:
            return None;
        
        mid = self.findMid(head);
        node = TreeNode(mid.val);
        if mid!=head:
            curr = head;
            while curr.next!=mid:
                curr = curr.next;
            curr.next = None;
            node.left = self.sortedListToBST(head);
        else:
            node.left = None;
        node.right = self.sortedListToBST(mid.next);
        
        return node;
        
    
    def findMid(self, head):
        if not head:
            return None;
        slow = fast = head;
        while fast!=None and fast.next!=None:
            slow = slow.next;
            fast = fast.next.next;
        
        return slow;
    


def sortedListToBST(self, head):
    if not head:
        return 
    if not head.next:
        return TreeNode(head.val)
    # here we get the middle point,
    # even case, like '1234', slow points to '2',
    # '3' is root, '12' belongs to left, '4' is right
    # odd case, like '12345', slow points to '2', '12'
    # belongs to left, '3' is root, '45' belongs to right
    slow, fast = head, head.next.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # tmp points to root
    tmp = slow.next
    # cut down the left child
    slow.next = None
    root = TreeNode(tmp.val)
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(tmp.next)
    return root