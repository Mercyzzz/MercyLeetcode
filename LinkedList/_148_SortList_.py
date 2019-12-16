# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        pre = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(pre)
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = tmp = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        print l1 or l2
        if l1:
            tmp.next = l1
        else:
            tmp.next = l2
        return dummy.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)
n4 = ListNode(3)

n1.next = n2
n2.next = n3
n3.next = n4

print Solution().sortList(n1)

