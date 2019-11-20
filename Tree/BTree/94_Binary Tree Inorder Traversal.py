# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret
        stack = []
        while root or len(stack) > 0:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ret.append(root.val)
                root = root.right
        return ret


    def dfs(self, root, ret):
        if not root:
            return
        if root.left:
            self.dfs(root.left, ret)
        ret.append(root.val)
        if root.right:
            self.dfs(root.right, ret)
