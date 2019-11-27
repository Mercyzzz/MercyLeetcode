# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

    def dfs(self, n, tep, ret):
        if len(n) == 0:
            ret.append(tep)
        for i in range(len(n)):
            self.dfs(n[:i] + n[i + 1:], tep + [n[i]], ret)

