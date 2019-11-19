# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before, after = ListNode(-1), ListNode(-1)
        beforeHead = before
        afterHead = after
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = afterHead.next
        return beforeHead.next


n1 = ListNode(6)
n2 = ListNode(4)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(5)
n6 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

n1 = Solution().partition(n1, 3)

while n1:
    print n1.val
    n1 = n1.next
