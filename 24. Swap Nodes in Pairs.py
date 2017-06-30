# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head;
        while curr!=None and curr.next != None:
            prev = curr
            curr = curr.next;
            nxt = curr.next;
            prev.val, curr.val = curr.val, prev.val;
            curr = nxt;
        
        return head;