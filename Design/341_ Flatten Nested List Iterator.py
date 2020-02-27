# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flist = []
        self.curIdx = 0
        def dfs(nlist):
            for i in nlist:
                if isinstance(i, list):
                    dfs(i)
                else:
                    self.flist.append(i)
        dfs(nestedList)

    def next(self):
        """
        :rtype: int
        """
        ret = self.flist[self.curIdx]
        self.curIdx += 1
        return ret


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.curIdx < len(self.flist):
            return True
        else:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# a = NestedIterator([[1,1],2,[1,1]])
# v = []
# while a.hasNext():
#     v.append(a.next())
# print v
nestedList = [[1,1],2,[1,1]]
i, v = NestedIterator(nestedList), []
while i.hasNext():
    v.append(i.next())
print v