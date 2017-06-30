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
        dummy = ListNode(-1);
        prev = dummy;
        prev.next = head;
        curr = head;
        while curr!=None and curr.next!=None:
            nxt = curr.next;
            if nxt.val!=curr.val:
                prev = curr;
                curr = nxt;
            else:
                val = curr.val;
                while curr!=None and curr.val==val:
                    curr = curr.next;
                prev.next = curr;
        
        return dummy.next;