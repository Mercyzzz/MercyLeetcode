# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        cur, pre = head2, None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        cur1, cur2 = head, pre
        while cur2:
            nex1, nex2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = nex1
            cur1, cur2 = nex1, nex2

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
Solution().reorderList(n1)