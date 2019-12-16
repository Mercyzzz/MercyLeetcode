# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        stack = []
        while root:
            if root.left and root.right:
                stack.append(root.right)
            if root.left:
                root.right = root.left
                root.left = None
            if not root.right and stack:
                root.right = stack.pop()
            root = root.right
    def flatten1(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        while stack:
            top = stack.pop()
            if top.left:
                tep = top.left
                while tep.right:
                    tep = tep.right
                tep.right = top.right
                top.right = top.left
                top.left = None
            if top.right:
                stack.append(top.right)

