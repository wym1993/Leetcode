# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k<2:
            return head;
        
        dummy = head;
        dummy_tail = None;
        changeHead = False;
        while dummy:
            tmp = dummy;
            for _ in range(k-1):
                if not tmp:
                    return head;
                tmp = tmp.next;
            
            if not tmp:
                return head;
            next_tmp = tmp.next;
            tmp.next = None;
            new_dummy, last_dummy = self.reverseList(dummy);
            if not changeHead:
                head = new_dummy;
                changeHead = True;
            else:
                dummy_tail.next = new_dummy;
            
            last_dummy.next = next_tmp;
            dummy, dummy_tail = next_tmp, last_dummy;
        
        return head;

    def reverseList(self, head):
        dummy=tail = None;
        while head:
            tmp = head.next;
            head.next = dummy;
            dummy = head;
            if not tail:
                tail = dummy;
            head = tmp;
        
        return dummy, tail;
            
                
            
                