# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

    def reverseListIte(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, cur = head, head.next
        pre.next = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

a = Solution().reverseList(a)

while a:
    print a.val
    a = a.next