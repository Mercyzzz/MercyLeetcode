# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node, level, res):
            if not node:
                return
            if len(res) < level:
                res.append([])
            res[level - 1].append(node.val)
            dfs(node.left, level + 1, res)
            dfs(node.right, level + 1, res)

        res = []
        dfs(root, 1, res)
        return res

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, cur_level = [], [root]
        while cur_level:
            next_level, tmp_res = [], []
            for node in cur_level:
                tmp_res.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(tmp_res)
            cur_level = next_level
        return res


root = TreeNode(3)
n1 = TreeNode(9)
n2 = TreeNode(20)
n3 = TreeNode(15)
n4 = TreeNode(7)
root.left = n1
root.right = n2
n2.left = n3
n2.right = n4
print Solution().levelOrder(root)
