# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        arr = [(p, q)]
        while arr:
            p, q = arr.pop()
            if not check(p, q):
                return False
            if p:
                arr.append((p.left, q.left))
                arr.append((p.right, q.right))
        return True
