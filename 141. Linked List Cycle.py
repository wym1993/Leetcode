# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        store = {}
        if not head or head.next==None:
            return False;
        
        temp = head;
        while temp!=None:
            if not temp in store:
                store[temp] = temp.next;
                temp = temp.next;
            else:
                return True;
        
        return False;