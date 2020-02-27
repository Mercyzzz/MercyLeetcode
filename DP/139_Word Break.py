class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i, -1, -1):
                if dp[j] and s[j:i + 1] in wordDict:
                    dp[i + 1] = True
                    break
        return dp[n]

    def wordBreakrec(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.dfs(s, wordDict)

    def dfs(self, remain, wordDict):
        if not remain:
            return True
        for word in wordDict:
            if remain[0:len(word)] != word:
                continue
            if self.dfs(remain[len(word):], wordDict):
                return True

        return False


print Solution().wordBreakrec("aaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
