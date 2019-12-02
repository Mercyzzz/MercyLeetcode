# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(None)
        dummy.next = head
        cur = head.next
        pre = head
        while cur:
            hn = dummy
            nodeVal = cur.val
            if nodeVal >= pre.val:
                cur = cur.next
                pre = pre.next
                continue
            else:
                while hn.next:
                    if nodeVal < hn.next.val:
                        hnNex, curNex = hn.next, cur.next
                        hn.next = cur
                        cur.next = hnNex
                        pre.next = curNex
                        cur = curNex
                        break
                    hn = hn.next
        return dummy.next

    def printAll(self, head):
        cur = head
        while cur:
            print cur.val
            cur = cur.next


n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(1)
n4 = ListNode(3)
n1.next = n2
#n2.next = n3
#n3.next = n4
a = Solution()
head = a.insertionSortList(n1)
a.printAll(head)


