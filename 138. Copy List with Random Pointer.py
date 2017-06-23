# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None;
        
        nMap = {};
        nHead = RandomListNode(head.label);
        nMap[head] = nHead;
        p = head;
        q = nHead;
        while p!=None:
            q.random = p.random;
            if p.next!=None:
                q.next = RandomListNode(p.next.label);
            else:
                q.next = None;
            nMap[p.next] = q.next;
            p = p.next;
            q = q.next;
        
        p =nHead;
        while p!=None:
            if p.random!=None:
                p.random = nMap[p.random];
            p = p.next;
        
        return nHead;
            