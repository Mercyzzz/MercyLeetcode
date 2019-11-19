class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs([(i + 1) for i in range(n)], k, [], ret)
        return ret

    def dfs(self, target, k, tep, ret):
        if k == 0:
            ret.append(tep)
        for i in range(len(target)):
            self.dfs(target[i + 1:], k - 1, tep + [target[i]], ret)


print Solution().combine(4, 2)
