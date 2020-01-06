# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        return self.recur(root)

    def recur(self, root):
        if not root:
            return
        val = self.recur(root.left)
        if self.k == 0:
            return val
        self.k = self.k - 1
        if self.k == 0:
            return root.val
        return self.recur(root.right)


n1 = TreeNode(5)
n2 = TreeNode(3)
n3 = TreeNode(6)
n4 = TreeNode(2)
n5 = TreeNode(4)
n6 = TreeNode(1)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n4.left = n6
print Solution().kthSmallest(n1, 4)
