# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        self.path(root, [], sum, ret)
        return ret

    def path(self, root, tep, sum, ret):
        if not root:
            return
        sum -= root.val
        if not root.left and not root.right and sum == 0:
            ret.append(tep + [root.val])
        if root.left:
            self.path(root.left, tep + [root.val], sum - root.val, ret)
        if root.right:
            self.path(root.right, tep + [root.val], sum - root.val, ret)

n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(8)
n4 = TreeNode(11)
n5 = TreeNode(13)
n6 = TreeNode(4)
n7 = TreeNode(7)
n8 = TreeNode(2)
n9 = TreeNode(5)
n10 = TreeNode(1)

n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n4.left = n7
n4.right = n8
n6.left = n9
n9.right = n10

print Solution().pathSum(n1, 22)
