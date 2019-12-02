# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodeArr = []
        self.dfs(root)
        self.top = 0

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.nodeArr.append(root.val)
        self.dfs(root.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.top < len(self.nodeArr):
            node = self.nodeArr[self.top]
            self.top += 1
            return node
        else:
            return False

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.top < len(self.nodeArr):
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()



root = TreeNode(7)
n1 = TreeNode(3)
n2 = TreeNode(15)
n3 = TreeNode(9)
n4 = TreeNode(20)
root.left = n1
root.right = n2
n2.left = n3
n2.right = n4
iterator = BSTIterator(root)
iterator.next()
iterator.next()
iterator.hasNext()
iterator.next()
iterator.hasNext()
iterator.next()
iterator.hasNext()
iterator.next()
iterator.hasNext()