"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        h = [];
        for i, list in enumerate(lists):
            if list:
                heapq.heappush(h, (list.val, i));
        
        dummy = ListNode(-1);
        head = dummy;
        while h:
            (minVal, minIdx) = heapq.heappop(h);
            head.next = ListNode(minVal);
            head = head.next;
            if lists[minIdx].next:
                lists[minIdx] = lists[minIdx].next;
                heapq.heappush(h, (lists[minIdx].val, minIdx));
        
        return dummy.next;

