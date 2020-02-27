class Solution:
    def kmp(self, s, p):
        next = self.nextArr(s)
        print next
        return self.match(s, p, next)

    def match(self, s, p, next):
        i = j = 0
        while i < len(s) and j < len(p):
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(p):
            return i - j
        else:
            return -1

    def nextArr(self, s):
        next = [0] * len(s)
        next[0] = -1
        pre, post = -1, 0
        while post < len(s) - 1:
            if pre == -1 or s[pre] == s[post]:
                pre += 1
                post += 1
                next[post] = pre
            else:
                pre = next[pre]
        return next


print Solution().kmp('ABCDABCABAABCD', 'BCD')
