# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None;
        
        l = 0;
        curr = head;
        while curr!=None:
            curr = curr.next;
            l+=1;
        k = k%l
        
        for _ in range(k):
            dummy = ListNode(-1);
            prev = dummy
            prev.next = head;
            curr = head;
            while curr.next!=None:
                curr = curr.next;
                prev = prev.next;
            
            val = curr.val;
            prev.next = None;
            dummy.val = val;
            head = dummy;
            
        return head;



class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        if head.next == None:
            return head
            
        pointer = head
        length = 1
        
        while pointer.next:
            pointer = pointer.next
            length += 1
        
        rotateTimes = k%length
        
        if k == 0 or rotateTimes == 0:
            return head
        
        fastPointer = head
        slowPointer = head
        
        for a in range (rotateTimes):
            fastPointer = fastPointer.next
        
        
        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        
        temp = slowPointer.next
        
        slowPointer.next = None
        fastPointer.next = head
        head = temp
        
        return head