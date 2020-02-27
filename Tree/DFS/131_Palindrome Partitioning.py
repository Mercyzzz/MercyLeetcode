class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs(s, 0, [])
        return self.res

    def dfs(self, s, start, tep):
        if start == len(s):
            self.res.append(tep)
            return
        for i in range(start, len(s)):
            if not self.isPalindrome(s, start, i):
                continue
            self.dfs(s, i + 1, tep + [s[start: i + 1]])

    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


print Solution().partition('aa')
