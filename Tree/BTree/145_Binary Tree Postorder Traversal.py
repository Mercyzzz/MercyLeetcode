# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        pre = root
        res = []
        while stack:
            cur = stack[-1]
            if (not cur.left and not cur.right) or cur.left == pre or cur.right == pre:
                res.append(cur.val)
                stack.pop()
                pre = cur
            else:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return res