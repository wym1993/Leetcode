# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None;
        
        dummy = ListNode(-1);
        dummy.next = head;
        prev = dummy;
        curr = head;
        while curr!=None:
            if curr.val==val:
                prev.next = curr.next;
                curr = prev.next;
            else:
                prev = curr;
                curr = curr.next
        
        return dummy.next;