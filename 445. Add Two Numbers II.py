# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, head):
        prev, curr = None, head;
        while curr:
            prev, curr.next, curr = curr, prev, curr.next;
        
        return prev;
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1);
        curr = dummy
        l1 = self.reverse(l1);
        l2 = self.reverse(l2);
        carry = 0;
        while l1!=None or l2!=None or carry:
            num1 = l1.val if l1 else 0;
            num2 = l2.val if l2 else 0;
            curr.next, carry = ListNode((num1+num2+carry)%10), (num1+num2+carry)/10
            l1 = l1.next if l1 else None;
            l2 = l2.next if l2 else None;
            curr = curr.next
        
        return self.reverse(dummy.next);
            

def addTwoNumbers(self, l1, l2):

        x1, x2 = 0, 0
        while l1:
            x1 = x1*10+l1.val
            l1 = l1.next
        while l2:
            x2 = x2*10+l2.val
            l2 = l2.next
        x = x1 + x2
        
        head = ListNode(0)
        if x == 0: return head
        while x:
            v, x = x%10, x//10
            head.next, head.next.next = ListNode(v), head.next
            
        return head.next