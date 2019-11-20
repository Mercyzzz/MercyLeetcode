# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 1)

    def dfs(self, root, level):
        if not root:
            return level - 1
        left, right = level, level
        if root.left:
            left = self.dfs(root.left, level + 1)
        if root.right:
            right = self.dfs(root.right, level + 1)
        return max(left, right)



root = TreeNode(3)
n1 = TreeNode(9)
n2 = TreeNode(20)
n3 = TreeNode(15)
n4 = TreeNode(7)
root.left = n1
root.right = n2
n2.left = n3
n2.right = n4
print Solution().maxDepth(root)
