# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, root, lower, upper):
        if not root:
            return True
        if root.val >= upper or root.val <= lower:
            return False
        return self.dfs(root.left, lower, root.val) and self.dfs(root.right, root.val, upper)

n1 = TreeNode(10)
n2 = TreeNode(5)
n3 = TreeNode(15)
n4 = TreeNode(6)
n5 = TreeNode(20)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
# n1.right = n3
# n3.left = n4
# n3.right = n5

print Solution().isValidBST(n1)