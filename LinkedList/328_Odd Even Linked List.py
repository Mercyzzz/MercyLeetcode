# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        evenHead = head.next
        dummyOdd = ListNode(-1)
        dummyEven = ListNode(-1)
        dummyOdd.next = head
        dummyEven.next = evenHead
        while evenHead and evenHead.next:
            head.next = evenHead.next
            head = head.next
            evenHead.next = head.next
            evenHead = evenHead.next
        head.next = dummyEven.next
        return dummyOdd.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

ret = Solution().oddEvenList(n1)

while ret:
    print ret.val
    ret = ret.next
