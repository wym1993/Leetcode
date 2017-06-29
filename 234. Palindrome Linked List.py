# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tmp = head;
        newHead = self.reverse(head);
        while tmp!=None:
            # print tmp.val, newHead.val
            if not newHead.val==tmp.val:
                return False;
            else:
                newHead = newHead.next;
                tmp = tmp.next;
        
        return True;
    
    def reverse(self, head):
        prev = None;
        curr = head;
        while curr!=None:
            new = ListNode(curr.val);
            # nxt = curr.next;
            new.next = prev;
            prev = new;
            curr = curr.next;
        
        return prev;



def isPalindrome(self, head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev