# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1);
        prev = dummy;
        prev.next = head;
        curr = head;
        
        for _ in range(m-1):
            curr = curr.next;
            prev = prev.next;
        
        for _  in range(n-m):
            curr = curr.next;
        
        nxt = curr.next;
        curr.next = None;
        nHead = self.reverse(prev.next);
        prev.next = nHead;
        while nHead.next!=None:
            nHead = nHead.next;
        nHead.next = nxt;
        
        return dummy.next;
    
    def reverse(self, head):
        pre = None;
        curr = head;
        while curr!=None:
            nxt = curr.next;
            curr.next = pre;
            pre = curr
            curr = nxt;
        
        return pre
        