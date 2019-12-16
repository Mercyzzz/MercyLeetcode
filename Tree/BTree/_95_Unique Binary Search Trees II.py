# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TrueeNode]
        """



    def _generateTrees(self, start, end):
        if start > end:
            return []
        res = []
        for i in range(start, end + 1):
            left = self._generateTrees(start, i - 1)
            right = self._generateTrees(i + 1, end)
            root = TreeNode(i)
            for l in left:
                for r in right:
                    root.left = l
                    root.right = r
                    res.append(root)

        return res