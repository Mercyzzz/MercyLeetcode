# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        newHead = Node(head.val, None, None)
        random = {}
        random[head] = newHead
        cur = head.next
        newCur = newHead
        while cur:
            tep = Node(cur.val, None, None)
            newCur.next = tep
            random[cur] = tep
            cur = cur.next
            newCur = newCur.next
        cur = head
        newCur = newHead
        print random
        while cur:
            if cur.random:
                newCur.random = random[cur.random]
            newCur = newCur.next
            cur = cur.next
        return newHead



a1 = Node(7, None, None)
a2 = Node(13, None, None)
a3 = Node(11, None, None)
a4 = Node(10, None, None)
a5 = Node(1, None, None)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a2.random = a1
a3.random = a5
a4.random = a3
a5.random = a1
print Solution().copyRandomList(a1)
print a1
