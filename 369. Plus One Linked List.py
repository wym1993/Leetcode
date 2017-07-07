# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
        
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head;
        while curr:
            prev, curr.next, curr = curr, prev, curr.next;
        
        digit = 1;
        curr = prev;
        dummy = None;
        while curr:
            dummy, curr.val, digit = curr, (curr.val+digit)%10, (curr.val+digit)/10;
            curr = curr.next;
        
        if digit:
            dummy.next = ListNode(digit);
        
        prev, curr = None, prev;
        while curr:
            prev, curr.next, curr = curr, prev, curr.next;
        
        return prev;
            
        
def plusOne(self, head):
    tail = None
    while head:
        head.next, head, tail = tail, head.next, head
    carry = 1
    while tail:
        carry, tail.val = divmod(carry + tail.val, 10)
        if carry and not tail.next:
            tail.next = ListNode(0)
        tail.next, tail, head = head, tail.next, tail
    return head