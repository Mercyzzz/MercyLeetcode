# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        pt = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tep = ListNode(l1.val)
                l1 = l1.next
            else:
                tep = ListNode(l2.val)
                l2 = l2.next
            pt.next = tep
            pt = pt.next
        if l1:
            pt.next = l1
        if l2:
            pt.next = l2
        return dummy.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)
n4 = ListNode(1)
n5 = ListNode(3)
n6 = ListNode(4)
n6 = ListNode(4)
n1.next = n2
n2.next = n3

dummy = Solution().mergeTwoLists(n1, n4)

while dummy:
    print dummy.val
    dummy = dummy.next
