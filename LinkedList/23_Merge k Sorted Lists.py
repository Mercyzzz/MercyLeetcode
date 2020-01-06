import json


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        count = len(lists.val)
        if count == 1:
            return lists[0]
        left = self.mergeKLists(lists[0:count // 2])
        right = self.mergeKLists(lists[count // 2:])
        return self.mergeTwo(left, right)

    def mergeTwo(self, l1, l2):
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


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

lists = "[[1,4,5],[1,3,4],[2,6]]"
lists = stringToListNode(lists)
print lists.val
exit()
ret = Solution().mergeKLists(lists)

out = listNodeToString(ret)
print out
