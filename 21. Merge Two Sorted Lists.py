# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1);
        tmp = dummy;
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                tmp.next = ListNode(l1.val);
                l1 = l1.next;
            else:
                tmp.next = ListNode(l2.val);
                l2 = l2.next;
            tmp = tmp.next;
        
        if l1:
            tmp.next = l1;
        else:
            tmp.next = l2;
        
        return dummy.next;
        