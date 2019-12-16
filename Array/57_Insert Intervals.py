class Solution(object):
    def insert(self, intervals, newInterval):
        start, end = newInterval[0], newInterval[1]
        l, r = [], []
        for interval in intervals:
            if interval[1] < start:
                l += interval,
            elif interval[0] > end:
                r += interval,
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        return l + [[start, end]] + r


print Solution().insert([[1, 3], [6, 9]], [2, 5])
