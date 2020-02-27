# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    'iter'
    def lowestCommonAncestorIter(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

    "rec/ Non stack"
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self. lowestCommonAncestor(root.right, p, q)
        if not right:
            return left
        elif not left:
            return right
        else:
            return root



    "stack rec"
    def lowestCommonAncestorRcrStack(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stackP, stackQ = [], []
        self.push(root, p, stackP)
        print len(stackP)
        self.push(root, q, stackQ)
        pre = None
        while stackP and stackQ:
            pNode = stackP.pop()
            qNode = stackQ.pop()
            if pNode != qNode:
                break
            pre = pNode
        return pre

    def push(self, root, p, stack):
        if root == p:
            stack.append(root)
            return True
        if root.left and self.push(root.left, p, stack):
            stack.append(root)
            return True
        if root.right and self.push(root.right, p, stack):
            stack.append(root)
            return True

n1 = TreeNode(3)
n2 = TreeNode(5)
n3 = TreeNode(1)
n1.left = n2
n1.right = n3
n4 = TreeNode(6)
n5 = TreeNode(2)
n6 = TreeNode(0)
n7 = TreeNode(8)
n8 = TreeNode(7)
n9 = TreeNode(4)
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n5.left = n8
n5.right = n9
print Solution().lowestCommonAncestorRcrStack(n1, n4, n9).val