# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        cur = headA
        while cur.next:
            cur = cur.next
        cur.next = headA
        node = self.detectCycle(headB)
        cur.next = None
        return node

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                node = head
                while node != slow:
                    node = node.next
                    slow = slow.next
                return node
        return None
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        aLength, bLength = 0, 0
        curA, curB = headA, headB
        while curA:
            aLength += 1
            curA = curA.next
        while curB:
            bLength += 1
            curB = curB.next
        lengthDiff = abs(aLength - bLength)
        curA, curB = headA, headB
        if aLength >= bLength:
            for i in range(lengthDiff):
                curA = curA.next
        else:
            for i in range(lengthDiff):
                curB = curB.next

        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None