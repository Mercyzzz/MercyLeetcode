# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        self.maxSum(root)
        return self.res
    def maxSum(self, root):
        if not root:
            return 0
        left = max(self.maxSum(root.left), 0)
        right = max(self.maxSum(root.right), 0)
        self.res = max(self.res, left + right + root.val)
        return max(left, right) + root.val


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3

print Solution().maxPathSum(n1)