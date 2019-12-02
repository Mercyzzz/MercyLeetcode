# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        curLevel = [root]
        ret = [root.val]
        while curLevel:
            nextLevel = []
            for node in curLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if nextLevel:
                ret.append(nextLevel[-1].val)
            curLevel = nextLevel
        return ret


