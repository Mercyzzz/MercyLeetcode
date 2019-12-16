class Solution(object):
    def longestPalindrome(self, s):
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        if not s or len(s) < 1:
            return ''
        st, e = 0, 0
        for i in range(len(s)):
            len1 = expand(s, i, i)
            len2 = expand(s, i, i + 1)
            maxLen = max(len1, len2)
            if maxLen > e - st:
                st = i - (maxLen - 1) // 2
                e = i + maxLen // 2
        return s[st:e + 1]

    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right, length = 0, 0, 0
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        for i in reversed(range(len(dp))):
            dp[i][i] = True
            if i + 1 < len(s) and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if length < 2:
                    left, right, length = i, i + 1, 1
            for j in range(i, len(dp[0])):
                if j - i < 2:
                    continue
                if i + 1 < len(s) and j - 1 >= 0:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and j - i > length:
                    left, right, length = i, j, j - i
        return s[left:right + 1]


print Solution().longestPalindrome('dddddddd')
