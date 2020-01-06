# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

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
    def lowestCommonAncestorRcr(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):
            if not current_node:
                return False
            mid = current_node == p or current_node == q
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            if mid + left + right >= 2:
                self.ans = current_node
            return mid or left or right
        recurse_tree(root)
        return self.ans


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
print Solution().lowestCommonAncestorRcrStack(n1, n9, n3).val