# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        store = [];
        temp = head;
        while temp!=None:
            store.append(temp.val);
            temp = temp.next;
        
        store.sort();
        temp = head;
        for i in store:
            temp.val = i;
            temp = temp.next;
        return head;
            