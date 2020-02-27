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

    def reverseListInPlace(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        cur, next = head, head.next
        while next:
            cur.next = next.next
            next.next = dummy.next
            dummy.next = next
            next = cur.next
        return dummy.next

    def reverseHead(self, head):
        dummy = ListNode(-1)
        cur = head
        while cur:
            next = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = next
        return dummy.next

        # while cur:
        #     prev.next = cur.next
        #     cur.next = dummy.next
        #     dummy.next = cur
        #     cur = prev.next
        return dummy.next
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

a = Solution().reverseIter(a)

while a:
    print a.val
    a = a.next