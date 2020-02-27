# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        stack = [root]
        while stack:
            next = []
            for i in stack:
                if i:
                    i.left, i.right = i.right, i.left
                    next.append(i.left)
                    next.append(i.right)
            stack = next
        return root


    # def invertTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     if not root:
    #         return None
    #     root.left, root.right = root.right, root.left
    #     if root.left:
    #         self.invertTree(root.left)
    #     if root.right:
    #         self.invertTree(root.right)
    #     return root