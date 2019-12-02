# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ret

    def dfs(self, root, ret):
        if not root:
            return
        ret.append(root.val)
        self.dfs(root.left, ret)
        self.dfs(root.right, ret)

root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n5 = TreeNode(5)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n5

print Solution().preorderTraversal(root)