# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head;
        
        first = EvenList = ListNode(head.val);
        head = head.next;
        second = OddList = ListNode(head.val);
        head = head.next;
        idx = 0
        while head:
            if idx%2==0:
                first.next = ListNode(head.val);
                first = first.next;
            else:
                second.next = ListNode(head.val);
                second = second.next;
            head = head.next;
            idx+=1;
        
        first.next = OddList;
        return EvenList;



def oddEvenList(self, head):
    dummy1 = odd = ListNode(0)
    dummy2 = even = ListNode(0)
    while head:
        odd.next = head
        even.next = head.next
        odd = odd.next
        even = even.next
        head = head.next.next if even else None
    odd.next = dummy2.next
    return dummy1.next