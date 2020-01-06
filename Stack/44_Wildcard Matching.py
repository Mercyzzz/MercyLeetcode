class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        is_ = -1
        js = -1

        i = 0
        j = 0
        m = len(s)
        n = len(p)

        # while i<m and j<n:#
        while i < m:  # ensure tranverse all the char in s until the end
            if j < n and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            elif j < n and p[j] == "*":
                js = j
                is_ = i
                j += 1
            elif is_ >= 0:
                j = js + 1
                i = is_ + 1
                is_ += 1
            else:
                return False

        while j < n and p[j] == "*":
            j += 1

        return j == n and i == m

    def isMatchDp(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = p[j - 1] in [s[i - 1], '?'] and dp[i - 1][j - 1]
        return dp[-1][-1]

print Solution().isMatch('adceb', 'a*c*b')
