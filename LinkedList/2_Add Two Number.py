# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        placeholder = 0
        ret = 0
        pos = 0
        retHead = ListNode(-1)
        dummy = retHead
        while l1 or l2:
            l1Val = l1.val if l1 else 0
            if l1:
                l1 = l1.next
            l2Val = l2.val if l2 else 0
            if l2:
                l2 = l2.next
            sum = l1Val + l2Val
            if placeholder == 1:
                sum += 1
                placeholder = 0
            if sum >= 10:
                nodeVal = sum - 10
                placeholder = 1
            else:
                nodeVal = sum
            tep = ListNode(nodeVal)
            dummy.next = tep
            dummy = dummy.next
            pos += 1
        if placeholder == 1:
            tep = ListNode(1)
            dummy.next = tep
        return retHead.next


l1 = ListNode(5)
l2 = ListNode(4)
l3 = ListNode(3)
r1 = ListNode(5)
r2 = ListNode(6)
r3 = ListNode(4)
#l1.next = l2
#l2.next = l3
#r1.next = r2
ret =  Solution().addTwoNumbers(l1, r1)
while ret:
    print ret.val
    ret = ret.next
