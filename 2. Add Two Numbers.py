# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1);
        curr = dummy;
        digit = 0;
        while l1!=None or l2!=None:
            val1 = 0 if l1==None else l1.val;
            val2 = 0 if l2==None else l2.val;
            val = (val1+val2+digit)%10;
            curr.next = ListNode(val);
            curr = curr.next;
            if l1:
                l1 = l1.next;
            if l2:
                l2 = l2.next

            digit = (val1+val2+digit)/10;
        
        if digit:
            curr.next = ListNode(1);
        return dummy.next;
        
        