# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next==None:
            return head;
        
        curr = head;
        nxt = head.next;
        while nxt!=None:
            while nxt!=None and curr.val==nxt.val:
                nxt = nxt.next;
            
            if nxt==None:
                curr.next = None;
                break;
            else:
                curr.next = nxt;
                curr = curr.next;
                nxt = nxt.next;
        
        return head;


class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head