# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre, after = dummy, dummy
        for i in range(m - 1):
            pre = pre.next
        for i in range(n + 1):
            after = after.next

        tepDummy = pre
        prevNode = tepDummy.next
        pCur = prevNode.next
        while pCur:
            if pCur == after:
                break
            prevNode.next = pCur.next
            pCur.next = tepDummy.next
            tepDummy.next = pCur
            pCur = prevNode.next
        return dummy.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

n1 = Solution().reverseBetween(n1, 1, 2)

while n1:
    print n1.val
    n1 = n1.next
