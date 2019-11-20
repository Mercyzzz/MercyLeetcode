class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.dfs(0, 0, n, '', ret)
        return ret

    def dfs(self, left, right, n, cur, res):
        if left == right == n:
            res.append(cur)
            return
        if left < n:
            self.dfs(left + 1, right, n, cur + '(', res)
        if right < left:
            self.dfs(left, right + 1, n, cur + ')', res)
