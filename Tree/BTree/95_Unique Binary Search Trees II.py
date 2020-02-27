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
        if n == 0:
            return []
        return self._generateTrees(1, n)

    def _generateTrees(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        for i in range(start, end + 1):
            left = self._generateTrees(start, i - 1)
            right = self._generateTrees(i + 1, end)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def treeNodeArrayToString(treeNodeArray):
    serializedTreeNodes = []
    for treeNode in treeNodeArray:
        serializedTreeNode = treeNodeToString(treeNode)
        serializedTreeNodes.append(serializedTreeNode)
    return "[{}]".format(', '.join(serializedTreeNodes))


n = 3
ret = Solution().generateTrees(n)
print ret
out = treeNodeArrayToString(ret)
print out