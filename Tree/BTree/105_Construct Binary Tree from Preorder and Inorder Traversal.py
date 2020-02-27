# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def build(self, preorder, inorder, pLeft, pRight, iLeft, iRight):
        if pLeft > pRight or iLeft > iRight:
            return None
        for i in range(iLeft, iRight + 1):
            if preorder[pLeft] == inorder[i]:
                aim = i
                break
        cur = TreeNode(preorder[pLeft])
        cur.left = self.build(preorder, inorder, pLeft + 1, pLeft + aim - iLeft, iLeft, aim - 1)
        cur.right = self.build(preorder, inorder, pLeft + aim - iLeft + 1, pRight, aim + 1, iRight)
        return cur