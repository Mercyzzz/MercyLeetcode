# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        pre = dummy
        cur = pre
        dummy.next = head
        num = 0
        while cur.next:
            cur = cur.next
            num += 1
        while num >= k:
            cur = pre.next
            for i in range(k - 1):
                next = cur.next
                cur.next = next.next
                next.next = pre.next
                pre.next = next
            pre = cur
            num -= k
        return dummy.next


    # def reverseKGroup(self, head, k):
    #     """
    #     :type head: ListNode
    #     :type k: int
    #     :rtype: ListNode
    #     """
    #     if not head or not head.next:
    #         return head
    #     pre = head
    #     dummy = None
    #     tail = None
    #     while pre and pre.next:
    #         cur = pre.next
    #         preTail = tail
    #         tail = pre
    #         tep = pre
    #         for i in range(k - 1):
    #             tep = tep.next
    #             if not tep:
    #                 return dummy if dummy else pre
    #         pre.next = None
    #         for i in range(k - 1):
    #             next = cur.next
    #             cur.next = pre
    #             pre = cur
    #             cur = next
    #         tail.next = cur
    #         if preTail:
    #             preTail.next = pre
    #         if not dummy:
    #             dummy = pre
    #         pre = cur
    #     return dummy



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
# b.next = c
# c.next = d
# d.next = e

ret = Solution().reverseKGroup(a, 3)
while ret:
    print ret.val
    ret = ret.next
