class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)

    def dfs(self, root, sum):
        if not root:
            return 0
        sum = sum * 10 + root.val
        if not root.left and not root.right:
            return sum
        sleft = self.dfs(root.left, sum)
        sright = self.dfs(root.right, sum)
        return sleft + sright
root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n5 = TreeNode(5)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n5
print Solution().sumNumbers(root)