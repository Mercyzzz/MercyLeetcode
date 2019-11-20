class Solution(object):
    digit2letters = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = []
        bfs = self.bfs(digits, [])
        self.dfs(digits, "", ret)
        return dfs

    def bfs(self, digits, res):
        if not digits:
            return res
        num = digits[0]
        tep = []
        str = self.digit2letters[num]
        if not res:
            return self.dfs(digits[1:], [i for i in str])

        for r in res:
            for c in str:
                tep.append(r + c)
        return self.dfs(digits[1:], tep)

    def dfs(self, digits, current, result):
        if not digits:
            result.append(current)
            return
        for c in self.digit2letters[digits[0]]:
            self.dfs(digits[1:], current + c, result)


print Solution().letterCombinations('23')
