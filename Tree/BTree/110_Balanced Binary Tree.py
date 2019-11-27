# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def length(root):
            if not root:
                return 0
            left = length(root.left) + 1
            right = length(root.right) + 1
            if abs(left - right) >= 2 or left == 0 or right == 0:
                return -1
            return max(left, right)
        return True if length(root) > 0 else False

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)

n1.left = n2
n2.left = n3
n3.left = n4
n4.left = n5

# n1.right = n3
# n3.left = n4
# n3.right = n5

print Solution().isBalanced(n1)