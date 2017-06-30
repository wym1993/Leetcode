# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1);
        prev = dummy;
        prev.next = head;
        curr = head;
        for _ in range(n-1):
            curr = curr.next;
        
        while curr.next!=None:
            curr = curr.next;
            prev = prev.next;
        
        prev.next = prev.next.next;
    
        return dummy.next;