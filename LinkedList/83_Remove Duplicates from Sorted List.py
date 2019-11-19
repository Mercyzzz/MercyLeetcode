# class ListNode(object):
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(1)
n4 = ListNode(2)
n5 = ListNode(3)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

n1 = Solution().deleteDuplicates(n1)

while n1:
    print n1.val
    n1 = n1.next

