class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashset = set()
        left, right, length = 0, 0, 0
        while left < len(s) and right < len(s):
            if s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            else:
                hashset.add(s[right])
                right += 1
            length = max(right - left, length)
        return length


print Solution().lengthOfLongestSubstring('')
