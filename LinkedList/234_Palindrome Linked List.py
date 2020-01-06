# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next

        while cur and cur.next:
            next = cur.next
            cur.next = next.next
            next.next = slow.next
            slow.next = next
        slow = slow.next
        while slow:
            if slow.val != head.val:
                return False
            slow, head = slow.next, head.next
        return True

a = ListNode(1)
b = ListNode(3)
c = ListNode(3)
d = ListNode(1)
#a.next = b
b.next = c
c.next = d

print Solution().isPalindrome(a)
