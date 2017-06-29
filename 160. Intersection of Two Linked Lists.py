# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None;
            
        newA = self.reverse(headA);
        newB = self.reverse(headB);
        prev = None;
        while newA!=None and newB!=None:
            if newA!=newB:
                break;
            else:
                prev = newA;
                newA = newA.next;
                newB = newB.next;
        
        return prev
    
    def reverse(self, head):
        curr = head;
        prev = None;
        while curr!=None:
            nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
        return prev



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        curA,curB = headA,headB
        lenA,lenB = 0,0
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        curA,curB = headA,headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA