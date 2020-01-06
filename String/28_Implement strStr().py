class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        next = [0] * (len(needle) + 1)
        next[0] = -1
        i, j = 0, -1
        while i < len(needle):
            while j != -1 and needle[i] != needle[j]:
                j = next[j]
            i += 1
            j += 1
            next[i] = j
        print next
        exit()
        i = j = 0
        while i < len(haystack) and j < len(needle):
            while j != -1 and haystack[i] != needle[j]:
                j = next[j]
            i += 1
            j += 1
        if j == len(needle):
            return i - j
        else:
            return -1

print Solution().strStr("abcabd", 'abababca')
